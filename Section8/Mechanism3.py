import pandas as pd
import numpy as np
from pathlib import Path
from scipy.stats import norm
import json
import matplotlib.pyplot as plt

path = Path(__file__).parent

# -------------------------
# Configuration
# -------------------------
ims = ['PGA', 'Sa_0.33', 'Sa_0.7']

im_config = {
    'PGA':     {'imt_big': 'SA', 'period': '0.01'},
    'Sa_0.33': {'imt_big': 'SA', 'period': '0.33'},
    'Sa_0.7':  {'imt_big': 'SA', 'period': '0.7'},
}

# Taxonomy sequences — building_id ranges
tax_seq = [
    ("CR_LFINF_7_CDL_1H",  range(1,    142),   141),
    ("CR_LFINF_7_CDM_1H",  range(2406, 2434),   28),
    ("CR_LFINF_7_CDL_2H",  range(142,  969),   827),
    ("CR_LFINF_7_CDM_2H",  range(2434, 2626),  192),
    ("CR_LFINF_7_CDL_3H",  range(969,  1896),  927),
    ("CR_LFINF_7_CDM_3H",  range(2626, 2850),  224),
    ("CR_LFINF_7_CDL_4H",  range(1896, 2406),  510),
    ("CR_LFINF_7_CDM_4H",  range(2850, 2963),  113),
]

# Damage ratios
dam_ratio_file = pd.read_csv(path.parent / "GroundMotionFields/Dam_ratio.csv")
damage_ratios = np.array([
    dam_ratio_file.loc[dam_ratio_file["Dstates"] == f"DS{i}", "DR"].iloc[0]
    for i in range(1, 5)
])  # shape (4,)

# Replacement costs
repl_cost_file = pd.read_csv(path.parent / "GroundMotionFields/repl_cost.csv")
tax_to_repl = {
    row["TAXONOMY"].strip(): float(row["REPL_COST_BUILD_NONSTRUC_STRUCT"])
    for _, row in repl_cost_file.iterrows()
}


# -------------------------
# Load fragility
# -------------------------
def load_fragility(tax, im_name):
    cfg = im_config[im_name]
    json_fp = (
        path.parent / "outputs" / "MSA" / f"{tax}_dp04"
        / f"frags_msa_{cfg['imt_big']}({cfg['period']}).json"
    )
    medians = np.zeros(4)
    betas = np.zeros(4)
    try:
        with open(json_fp) as f:
            frag = json.load(f)
        for k, dls in enumerate(["DLS-1", "DLS-2", "DLS-3", "DLS-4"]):
            medians[k] = frag[dls]["median"]
            betas[k] = frag[dls]["beta"]
    except Exception as e:
        print(f"  Warning: {e}")
        medians[:] = np.nan
        betas[:] = np.nan
    return np.log(medians), betas


# -------------------------
# Load GMM mean per building per IM
# -------------------------
gmm_file = pd.read_csv(path / "GMM_results_expanded.csv")
gmm_file["building_id"] = (
    gmm_file["Building"]
    .str.replace("Building_", "", regex=False)
    .astype(int)
)
mean_col_map = {
    'PGA':     'mean_PGA',
    'Sa_0.33': 'mean_Sa_0.33',
    'Sa_0.7':  'mean_Sa_0.7',
}


# -------------------------
# Load GMF simulations per IM
# -------------------------
def load_gmf(im_name):
    if im_name == 'Sa_0.33':
        fname = "gmf_SA(0.33)_openquake_MAO2026_RandomSeed_50_mw6.3.csv"
    elif im_name == 'Sa_0.7':
        fname = "gmf_SA(0.7)_openquake_MAO2026_RandomSeed_50_mw6.3.csv"
    else:
        fname = "gmf_PGA_openquake_MAO2026_RandomSeed_50_mw6.3.csv"

    df = pd.read_csv(
        path.parent / "GroundMotionFields" / "final_files" / fname
    )
    df["building_id"] = (
        df["Building"]
        .str.replace("Building_", "", regex=False)
        .astype(int)
    )
    sim_cols = [c for c in df.columns if c.startswith("IM_sim")]
    return df, sim_cols


# -------------------------
# Compute P(DS=ds | eta) for all damage states
# returns shape (4, n_sim) for a single building
# -------------------------
def compute_pds(ln_eta_sims, ln_medians, betas):
    """
    ln_eta_sims : shape (n_sim,)
    ln_medians  : shape (4,)
    betas       : shape (4,)
    returns     : shape (4, n_sim) — P(DS=ds) for ds=1..4
    """
    n_sim = len(ln_eta_sims)
    # P(DS >= ds) for ds=1..4 — shape (4, n_sim)
    P_exceed = norm.cdf(
        (ln_eta_sims[np.newaxis, :] - ln_medians[:, np.newaxis])
        / betas[:, np.newaxis]
    )
    # P(DS = ds) = P(DS>=ds) - P(DS>=ds+1)
    P_ds = np.zeros((4, n_sim))
    for ds in range(4):
        if ds < 3:
            P_ds[ds] = P_exceed[ds] - P_exceed[ds + 1]
        else:
            P_ds[ds] = P_exceed[ds]
    return P_ds  # shape (4, n_sim)


# -------------------------
# Main computation
# -------------------------
results = []

for im_name in ims:
    print(f"\n{'='*50}")
    print(f"Processing IM: {im_name}")
    print(f"{'='*50}")

    gmf_df, sim_cols = load_gmf(im_name)
    n_sim = len(sim_cols)

    mean_col = mean_col_map[im_name]

    # Accumulators across all buildings — shape (n_sim,)
    sum_ell_j = np.zeros(n_sim)   # sum_i ell_{i,j}
    sum_xi2_j = np.zeros(n_sim)   # sum_i Var(xi_{i,j} | y_j)
    # = sum_i C_i^2 * Var(DR_i | eta_{i,j})

    for tax, bldg_range, N_tax in tax_seq:

        ln_medians, betas = load_fragility(tax, im_name)
        if np.any(np.isnan(ln_medians)):
            print(f"  Skipping {tax} — missing fragility")
            continue

        C_i = tax_to_repl.get(tax, np.nan)
        if np.isnan(C_i):
            print(f"  Skipping {tax} — missing replacement cost")
            continue

        for bldg_id in bldg_range:

            # Get GMF simulations for this building — shape (n_sim,)
            row = gmf_df[gmf_df["building_id"] == bldg_id]
            if len(row) == 0:
                continue
            im_vals = row[sim_cols].values[0]  # natural units
            ln_im = np.log(im_vals)   # log units, shape (n_sim,)

            # Compute P(DS=ds | eta_{i,j}) — shape (4, n_sim)
            P_ds = compute_pds(ln_im, ln_medians, betas)

            # Expected loss given
            # GMF: ell_{i,j} = C_i * sum_ds DR_ds * P(DS=ds)
            # shape (n_sim,)
            ell_ij = C_i * np.sum(
                damage_ratios[:, np.newaxis] * P_ds, axis=0
            )

            # E[DR_i^2 | eta] = sum_ds DR_ds^2 * P(DS=ds)
            E_DR2 = np.sum(
                (damage_ratios**2)[:, np.newaxis] * P_ds, axis=0
            )
            # E[DR_i | eta]^2
            E_DR_sq = (np.sum(
                damage_ratios[:, np.newaxis] * P_ds, axis=0
            ))**2

            # Var(DR_i | eta_{i,j}) — shape (n_sim,)
            Var_DR = E_DR2 - E_DR_sq

            # Accumulate
            sum_ell_j += ell_ij
            sum_xi2_j += (C_i**2) * Var_DR

    # -------------------------
    # Term 1: E[Var(L | y)] = E[sum_i C_i^2 * Var(DR_i | eta_{i,j})]
    # averaged over simulations
    # -------------------------
    Term1 = np.mean(sum_xi2_j)

    # -------------------------
    # Term 2: Var(E[L | y]) = Var(sum_i ell_{i,j})
    # variance of the expected loss across simulations
    # -------------------------
    Term2 = np.var(sum_ell_j, ddof=1)

    # -------------------------
    # Ratio Term1 / Term2 — should be small for large N
    # -------------------------
    ratio = Term1 / Term2

    # -------------------------
    # Total empirical Var(L) for verification
    # Load from precomputed file
    # -------------------------
    if im_name == 'Sa_0.33':
        loss_path = (path.parent / "GroundMotionFields/outputs_gmfs_repaircost"
                     / "repairs_per_sim_CombinedPeriod-Sa(0.33)_openquake_MAO2026_RandomSeed_50_mw6.3.csv")
    elif im_name == 'Sa_0.7':
        loss_path = (path.parent / "GroundMotionFields/outputs_gmfs_repaircost"
                     / "repairs_per_sim_CombinedPeriod-Sa(0.7)_openquake_MAO2026_RandomSeed_50_mw6.3.csv")
    else:
        loss_path = (path.parent / "GroundMotionFields/outputs_gmfs_repaircost"
                     / f"repairs_per_sim_CombinedPeriod-PGA_openquake_MAO2026_RandomSeed_50_mw6.3.csv")

    loss_df = pd.read_csv(loss_path)
    rep_cols = [c for c in loss_df.columns if c.startswith("Repair_sim")]
    L_j = loss_df[rep_cols].sum(axis=0).values
    Var_L_emp = np.var(L_j, ddof=1)

    print(f"  Term 1 — E[Var(L|y)]        : {Term1:.4e} USD²")
    print(f"  Term 2 — Var(E[L|y])        : {Term2:.4e} USD²")
    print(f"  Ratio Term1/Term2           : {ratio:.6f}")
    print(f"  Term1 + Term2 (analytical)  : {Term1+Term2:.4e} USD²")
    print(f"  Empirical Var(L)            : {Var_L_emp:.4e} USD²")
    print(f"  Term1 as % of Var_L_emp     : {Term1/Var_L_emp*100:.3f}%")
    print(f"  Term2 as % of Var_L_emp     : {Term2/Var_L_emp*100:.3f}%")

    results.append({
        "IM":          im_name,
        "Term1":       Term1,
        "Term2":       Term2,
        "ratio":       ratio,
        "Var_L_emp":   Var_L_emp,
        "Term1_pct":   Term1 / Var_L_emp * 100,
        "Term2_pct":   Term2 / Var_L_emp * 100,
    })

# -------------------------
# Summary table
# -------------------------
df_res = pd.DataFrame(results)
print("\n========== MECHANISM 3 SUMMARY ==========")
print(df_res[[
    "IM", "Term1", "Term2", "ratio", "Var_L_emp",
    "Term1_pct", "Term2_pct"
]].to_string(index=False))

# -------------------------
# Plot: ratio Term1/Term2 across IMs
# -------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(df_res["IM"], df_res["ratio"], color=["#2196F3", "#FF9800", "#4CAF50"])
axes[0].set_ylabel("Term 1 / Term 2")
axes[0].set_title("Ratio of idiosyncratic to\nground-motion-driven variance")
axes[0].axhline(0.01, color='red', linestyle='--', label='1% threshold')
axes[0].legend()
for i, v in enumerate(df_res["ratio"]):
    axes[0].text(i, v + 0.0002, f"{v:.4f}", ha='center', fontsize=10)

axes[1].bar(
    df_res["IM"],
    df_res["Term1_pct"],
    label="Term 1 (idiosyncratic)",
    color=["#2196F3", "#FF9800", "#4CAF50"],
    alpha=0.7
)
axes[1].set_ylabel("% of empirical Var(L)")
axes[1].set_title("Term 1 as % of total\nempirical variance")
axes[1].axhline(1.0, color='red', linestyle='--', label='1% threshold')
axes[1].legend()
for i, v in enumerate(df_res["Term1_pct"]):
    axes[1].text(i, v + 0.01, f"{v:.3f}%", ha='center', fontsize=10)

plt.tight_layout()
plt.savefig(path / "mechanism3_ratio.pdf", dpi=150)
plt.show()

df_res.to_csv(path / "mechanism3_results.csv", index=False)
print("\nSaved to mechanism3_results.csv and mechanism3_ratio.png")
