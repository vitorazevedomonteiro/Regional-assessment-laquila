import pandas as pd
import numpy as np
from pathlib import Path

path = Path(__file__).parent

ims = ['PGA', 'Sa_0.33', 'Sa_0.7']

results = []

for imt in ims:
    if imt == 'Sa_0.33':
        spcorr_path_openquake = (
            path.parent
            / "GroundMotionFields"
            / "outputs_gmfs_repaircost"
            / 'repairs_per_sim_CombinedPeriod-Sa(0.33)_openquake_MAO2026_RandomSeed_50_mw6.3.csv'
        )
    elif imt == 'Sa_0.7':
        spcorr_path_openquake = (
            path.parent
            / "GroundMotionFields"
            / "outputs_gmfs_repaircost"
            / 'repairs_per_sim_CombinedPeriod-Sa(0.7)_openquake_MAO2026_RandomSeed_50_mw6.3.csv'
        )
    elif imt == 'PGA':
        spcorr_path_openquake = (
            path.parent
            / "GroundMotionFields"
            / "outputs_gmfs_repaircost"
            / 'repairs_per_sim_CombinedPeriod-PGA_openquake_MAO2026_RandomSeed_50_mw6.3.csv'
        )

    repair_sim_spcorr_df_openquake = pd.read_csv(spcorr_path_openquake)

    repair_cols_spcorr_openquake = [
        c for c in repair_sim_spcorr_df_openquake.columns if
        c.startswith("Repair_sim")
    ]

    # L_j: aggregate loss per simulation — shape (n_sim,)
    L = repair_sim_spcorr_df_openquake[
        repair_cols_spcorr_openquake
    ].sum(axis=0).values

    # -------------------------
    # Empirical variance
    # -------------------------
    n_sim = len(L)
    mean_L = np.mean(L)
    var_L = np.var(L, ddof=1)   # unbiased estimator
    std_L = np.std(L, ddof=1)
    cv_L = std_L / mean_L      # coefficient of variation

    print(f"\n--- {imt} ---")
    print(f"  n_sim      : {n_sim}")
    print(f"  Mean L     : {mean_L:.4e} €")
    print(f"  Var(L)     : {var_L:.4e} €²")
    print(f"  Std(L)     : {std_L:.4e} €")
    print(f"  CV(L)      : {cv_L:.4f}")

    results.append({
        "IM":      imt,
        "n_sim":   n_sim,
        "mean_L":  mean_L,
        "var_L":   var_L,
        "std_L":   std_L,
        "cv_L":    cv_L,
    })

# -------------------------
# Summary
# -------------------------
df_results = pd.DataFrame(results)
print("\n========== EMPIRICAL VARIANCE SUMMARY ==========")
print(df_results[["IM", "mean_L", "var_L", "std_L", "cv_L"]].to_string(
    index=False))

# -------------------------
# Check invariance across IMs
# -------------------------
vals = df_results["var_L"].values
rel_diff = (vals.max() - vals.min()) / vals.mean() * 100
print(f"\nMax relative difference in empirical Var(L): {rel_diff:.2f}%")

# -------------------------
# Compare analytical vs empirical
# -------------------------
analytical = pd.read_csv(path / "full_variance_decomposition.csv")
df_compare = df_results.merge(
    analytical[["IM", "total_var_analytical"]], on="IM"
)
df_compare["ratio_emp_over_analytical"] = (
    df_compare["var_L"] / df_compare["total_var_analytical"]
)

print("\n========== ANALYTICAL vs EMPIRICAL ==========")
print(df_compare[[
    "IM", "var_L", "total_var_analytical", "ratio_emp_over_analytical"
]].to_string(index=False))

df_results.to_csv(path / "empirical_variance_loss.csv", index=False)
