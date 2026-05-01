import pandas as pd
import numpy as np
from pathlib import Path

path = Path(__file__).parent

# -------------------------
# Tau values per IM (inter-event std dev)
# -------------------------
tau = {
    'PGA':     0.255754164,
    'Sa_0.33': 0.261709745,
    'Sa_0.7':  0.266111546,
}

# -------------------------
# Files
# -------------------------
si_files = {
    'PGA':     path / "loss_sensitivity_PGA.csv",
    'Sa_0.33': path / "loss_sensitivity_Sa_0.33.csv",
    'Sa_0.7':  path / "loss_sensitivity_Sa_0.7.csv",
}

results = []

# -------------------------
# Load all datasets first (for consistency check)
# -------------------------
all_ids = None

for im_name, si_path in si_files.items():

    df = pd.read_csv(si_path)

    # Check building consistency
    ids = set(df["building_id"])

    if all_ids is None:
        all_ids = ids
    else:
        if ids != all_ids:
            print(f"WARNING: Building sets differ for {im_name}")

# -------------------------
# Main computation
# -------------------------
for im_name, si_path in si_files.items():

    print(f"\n--- Processing {im_name} ---")

    df = pd.read_csv(si_path)

    # -------------------------
    # Handle NaNs safely
    # -------------------------
    n_nan = df["s_i"].isna().sum()
    if n_nan > 0:
        print(f"  Warning: {n_nan} NaN s_i values → set to 0")
        df["s_i"] = df["s_i"].fillna(0.0)

    s_vals = df["s_i"].values

    # -------------------------
    # Core quantities
    # -------------------------
    sum_si = np.sum(s_vals)
    sum_si_sq = sum_si ** 2

    tau_im = tau[im_name]
    tau2 = tau_im ** 2

    between_event_var = tau2 * sum_si_sq

    # -------------------------
    # Diagnostics
    # -------------------------
    print(f"  N buildings           : {len(df)}")
    print(f"  sum(s_i)              : {sum_si:.4e}")
    print(f"  (sum s_i)^2           : {sum_si_sq:.4e}")
    print(f"  tau                   : {tau_im:.6f}")
    print(f"  tau^2                 : {tau2:.6f}")
    print(f"  Between-event Var(L)  : {between_event_var:.4e}")

    results.append({
        "IM": im_name,
        "tau": tau_im,
        "tau2": tau2,
        "N_buildings": len(df),
        "sum_si": sum_si,
        "sum_si_sq": sum_si_sq,
        "between_event_var": between_event_var,
    })

# -------------------------
# Summary
# -------------------------
df_results = pd.DataFrame(results)

print("\n========== SUMMARY ==========")
print(df_results[[
    "IM",
    "N_buildings",
    "tau",
    "sum_si",
    "between_event_var"
]].to_string(index=False))

# -------------------------
# Invariance check (CRITICAL)
# -------------------------
vals = df_results["between_event_var"].values
rel_diff = (vals.max() - vals.min()) / vals.mean() * 100

print(f"\nMax relative difference across IMs: {rel_diff:.2f}%")

# -------------------------
# Additional diagnostic
# -------------------------
print("\n--- Additional checks ---")
print("Variance of sum(s_i) across IMs:",
      np.var(df_results["sum_si"].values))

# -------------------------
# Save
# -------------------------
df_results.to_csv(
    path
    / "between_event_variance.csv", index=False)

print("\nSaved to between_event_variance.csv")
