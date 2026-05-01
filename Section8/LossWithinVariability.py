import pandas as pd
import numpy as np
from pathlib import Path

path = Path(__file__).parent

# -------------------------
# phi values per IM (intra-event std dev)
# -------------------------
phi = {
    'PGA':     0.569858696,
    'Sa_0.33': 0.621610596,
    'Sa_0.7':  0.600106996,
}

# -------------------------
# IM list
# -------------------------
ims = ['PGA', 'Sa_0.33', 'Sa_0.7']

results = []

for im_name in ims:

    print(f"\n--- Processing {im_name} ---")

    # -------------------------
    # Load sensitivities s_i
    # -------------------------
    si_df = pd.read_csv(path / f"loss_sensitivity_{im_name}.csv")
    si_df = si_df.dropna(subset=["s_i"])

    si_dict = dict(zip(si_df["building_id"], si_df["s_i"]))
    s_vals = si_df["s_i"].values

    sum_si = s_vals.sum()
    print(f"  N buildings : {len(si_df)}")
    print(f"  sum(s_i)    : {sum_si:.4e}")

    # -------------------------
    # Load correlations
    # -------------------------
    corr_df = pd.read_csv(path / f"Building_Pair_Correlations_{im_name}.csv")
    print(f"  N raw pairs : {len(corr_df)}")

    # Extract IDs
    corr_df["id1"] = (
        corr_df["Building1"].str.replace(
            "Building_", "", regex=False).astype(int)
    )
    corr_df["id2"] = (
        corr_df["Building2"].str.replace(
            "Building_", "", regex=False).astype(int)
    )

    # Map sensitivities
    corr_df["s_i"] = corr_df["id1"].map(si_dict)
    corr_df["s_k"] = corr_df["id2"].map(si_dict)

    # Drop missing
    n_before = len(corr_df)
    corr_df = corr_df.dropna(subset=["s_i", "s_k"])
    n_after = len(corr_df)

    if n_before != n_after:
        print(f"  Warning: dropped {n_before - n_after} invalid pairs")

    # -------------------------
    # Detect if pairs are symmetric
    # -------------------------
    pairs_unique = corr_df[["id1", "id2"]].drop_duplicates()
    is_symmetric = len(pairs_unique) != len(corr_df)

    print(f"  Symmetric pairs detected: {is_symmetric}")

    # -------------------------
    # OFF-DIAGONAL sum
    # -------------------------
    corr_df["contribution"] = corr_df["s_i"] * corr_df[
        "s_k"] * corr_df["Correlation"]
    off_diag = corr_df["contribution"].sum()

    print(f"  Off-diagonal sum           : {off_diag:.4e}")

    # -------------------------
    # DIAGONAL term (i = k)
    # rho(0) = 1 → s_i^2
    # -------------------------
    diag = np.sum(s_vals ** 2)
    print(f"  Diagonal sum (sum s_i^2)   : {diag:.4e}")

    # -------------------------
    # FULL double sum
    # -------------------------
    if is_symmetric:
        # pairs already include (i,k) and (k,i)
        numerator = diag + off_diag
    else:
        # pairs are only i < k → multiply by 2
        numerator = diag + 2 * off_diag

    print(f"  Full double sum numerator  : {numerator:.4e}")

    # -------------------------
    # Denominator
    # -------------------------
    denominator = sum_si ** 2
    print(f"  Denominator (sum_si)^2     : {denominator:.4e}")

    # -------------------------
    # Effective correlation
    # -------------------------
    rho_bar = numerator / denominator
    print(f"  rho_bar                   : {rho_bar:.6f}")

    # -------------------------
    # Within-event variance
    # -------------------------
    phi_im = phi[im_name]
    within_event_var = (phi_im ** 2) * numerator

    print(f"  phi                       : {phi_im:.6f}")
    print(f"  Within-event Var(L)       : {within_event_var:.4e}")

    results.append({
        "IM": im_name,
        "phi": phi_im,
        "sum_si": sum_si,
        "diag_sum": diag,
        "off_diag_sum": off_diag,
        "numerator": numerator,
        "denominator": denominator,
        "rho_bar": rho_bar,
        "within_event_var": within_event_var,
    })

# -------------------------
# Summary
# -------------------------
df_results = pd.DataFrame(results)

print("\n========== SUMMARY ==========")
print(df_results[[
    "IM", "phi", "sum_si", "rho_bar", "within_event_var"
]].to_string(index=False))

# -------------------------
# Mechanism 2 check
# -------------------------
df_results["phi2_rhobar"] = df_results["phi"]**2 * df_results["rho_bar"]

print("\n--- Mechanism 2 check: phi^2 * rho_bar ---")
print(df_results[["IM", "phi2_rhobar"]].to_string(index=False))

vals = df_results["phi2_rhobar"].values
rel_diff = (vals.max() - vals.min()) / vals.mean() * 100

print(f"\nMax relative difference in phi^2*rho_bar: {rel_diff:.2f}%")

# -------------------------
# Save
# -------------------------
df_results.to_csv(path / "within_event_variance.csv", index=False)

print("\nSaved to within_event_variance.csv")
