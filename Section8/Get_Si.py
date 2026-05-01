import pandas as pd
import numpy as np
import json
from pathlib import Path
from scipy.stats import norm

path = Path(__file__).parent

# Inputs
imt = 'SA'
period = 0.7

if imt == 'PGA':
    imt_big = 'SA'
    period = '0.01'
if imt == 'SA':
    imt_big = 'SA'
    imt_small = 'sa'
    period = period

# -------------------------
# Taxonomy sequences per building number range
# -------------------------
tax_seq = [
    ("CR_LFINF_7_CDL_1H", range(1, 142)),
    ("CR_LFINF_7_CDM_1H", range(2406, 2434)),
    ("CR_LFINF_7_CDL_2H", range(142, 969)),
    ("CR_LFINF_7_CDM_2H", range(2434, 2626)),
    ("CR_LFINF_7_CDL_3H", range(969, 1896)),
    ("CR_LFINF_7_CDM_3H", range(2626, 2850)),
    ("CR_LFINF_7_CDL_4H", range(1896, 2406)),
    ("CR_LFINF_7_CDM_4H", range(2850, 2963)),
]


def load_fragility_json(tax):
    base_path = (
        path.parent
        / "outputs"
        / "MSA"
        / f"{tax}_dp04"
    )
    json_fp = base_path / f"frags_msa_{imt_big}({period}).json"

    medians = np.zeros(4)
    betas = np.zeros(4)

    try:
        with open(json_fp, "r") as f:
            frag_data = json.load(f)
        for k, dls in enumerate(["DLS-1", "DLS-2", "DLS-3", "DLS-4"]):
            medians[k] = frag_data[dls]["median"]
            betas[k] = frag_data[dls]["beta"]
    except Exception as e:
        print(f"Warning: could not read fragility for {tax} at {json_fp}: {e}")
        medians[:] = np.nan
        betas[:] = np.nan

    return medians, betas


# -------------------------
# Damage ratios
# -------------------------
dam_ratio_file = pd.read_csv(path.parent / "GroundMotionFields/Dam_ratio.csv")
damage_ratios = [
    dam_ratio_file.loc[dam_ratio_file["Dstates"] == f"DS{i}", "DR"].iloc[0]
    for i in range(1, 5)
]
damage_ratio_per_DS = np.array(damage_ratios)  # shape (4,) for DS1..DS4

# -------------------------
# Replacement costs
# -------------------------
repl_cost_file = pd.read_csv(path.parent / "GroundMotionFields/repl_cost.csv")
tax_to_repl = {
    row["TAXONOMY"].strip(): float(row["REPL_COST_BUILD_NONSTRUC_STRUCT"])
    for _, row in repl_cost_file.iterrows()
}

# -------------------------
# Load GMM mean log-IM per building directly
# mean_PGA column is already mu_i = E[ln(PGA)] at each site
# -------------------------
gmm_file = pd.read_csv(path / "GMM_results_expanded.csv")

# Extract building index from "Building_1" -> 1
gmm_file["building_id"] = (
    gmm_file["Building"]
    .str.replace("Building_", "", regex=False)
    .astype(int)
)

# Select the correct mean column based on IM
if imt == 'PGA':
    mean_col = "mean_PGA"
elif imt == 'SA':
    mean_col = f"mean_Sa_{period}"

# Build dict: building_id -> mu_i (already in log space)
gmf_mean_dict = dict(zip(gmm_file["building_id"], gmm_file[mean_col]))

print(f"Loaded GMM means for {len(gmf_mean_dict)} buildings")
print(f"Example mu_i for Building_1: {gmf_mean_dict.get(1, 'NOT FOUND'):.4f}")


# -------------------------
# Loss sensitivity function
# -------------------------
def compute_si(mu_i, ln_medians, betas, DR, C_i):
    """
    Compute loss sensitivity s_i for a single building.

    Parameters
    ----------
    mu_i       : float — GMPE mean log-IM at site i (ln units)
    ln_medians : array — ln(fragility medians) for DS1..DS4, shape (4,)
    betas      : array — fragility dispersions for DS1..DS4, shape (4,)
    DR         : array — damage ratios for DS1..DS4, shape (4,)
    C_i        : float — replacement cost of building i

    Returns
    -------
    s_i : float — loss sensitivity (same units as C_i)
    """

    # Step 1: standardized argument z = (mu_i - ln_median) / beta
    z = (mu_i - ln_medians) / betas          # shape (4,)

    # Step 2: standard normal PDF at each z
    phi_z = norm.pdf(z)                       # shape (4,)

    # Step 3: derivative of P(DS>=ds) w.r.t. ln_IM = phi(z) / beta
    dphi_dbeta = phi_z / betas               # shape (4,)

    # Step 4: derivative of P(DS=ds) w.r.t. ln_IM
    # = dphi_dbeta[ds] - dphi_dbeta[ds+1]
    # last DS has no ds+1 term
    dP_ds = np.zeros(4)
    for ds in range(4):
        if ds < 3:
            dP_ds[ds] = dphi_dbeta[ds] - dphi_dbeta[ds + 1]
        else:
            dP_ds[ds] = dphi_dbeta[ds]

    # Step 5: s_i = C_i * sum_ds [ DR_ds * dP(DS=ds)/d(ln_IM) ]
    s_i = C_i * np.sum(DR * dP_ds)

    return s_i


# -------------------------
# Main loop: compute s_i for every building
# -------------------------
results = []

for tax, bldg_range in tax_seq:

    # Load fragility for this taxonomy
    medians, betas = load_fragility_json(tax)

    # Fragility medians are in natural units (g) -> convert to log space
    ln_medians = np.log(medians)

    # Replacement cost for this taxonomy
    C_i = tax_to_repl.get(tax, np.nan)
    if np.isnan(C_i):
        print(f"Warning: no replacement cost found for {tax}")

    for bldg_id in bldg_range:

        mu_i = gmf_mean_dict.get(bldg_id, np.nan)

        if np.isnan(mu_i):
            print(f"Warning: no GMF mean for building {bldg_id}")
            s_i = np.nan
        elif np.any(np.isnan(ln_medians)) or np.any(np.isnan(betas)):
            s_i = np.nan
        else:
            s_i = compute_si(
                mu_i=mu_i,
                ln_medians=ln_medians,
                betas=betas,
                DR=damage_ratio_per_DS,
                C_i=C_i
            )

        results.append({
            "building_id":  bldg_id,
            "taxonomy":     tax,
            "mu_i":         mu_i,
            "C_i":          C_i,
            "s_i":          s_i
        })

# -------------------------
# Save and summarize
# -------------------------
df_results = pd.DataFrame(results)
if imt == 'PGA':
    df_results.to_csv(path / f"loss_sensitivity_{imt}.csv", index=False)
elif imt == 'SA':
    df_results.to_csv(
        path / f"loss_sensitivity_{imt}_{period}.csv", index=False)

print(df_results.head(20).to_string())
print(f"\nTotal buildings processed : {len(df_results)}")
print(f"NaN count in s_i          : {df_results['s_i'].isna().sum()}")
print(f"Sum of s_i                : {df_results['s_i'].sum():.6f}")
print(f"(Sum of s_i)^2            : {df_results['s_i'].sum()**2:.6f}")
print(f"Mean s_i                  : {df_results['s_i'].mean():.6f}")
