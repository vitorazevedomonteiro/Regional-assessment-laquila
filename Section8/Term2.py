import pandas as pd
from pathlib import Path
import numpy as np

path = Path(__file__).parent

# -------------------------
# Load both results files
# -------------------------
between_df = pd.read_csv(path / "between_event_variance.csv")
within_df = pd.read_csv(path / "within_event_variance.csv")

# -------------------------
# Merge on IM
# -------------------------
df = between_df.merge(
    within_df[["IM", "rho_bar", "within_event_var", "phi2_rhobar"]],
    on="IM",
    how="inner"
)

# -------------------------
# Rename for clarity (match theory)
# -------------------------
df = df.rename(columns={
    "between_event_var": "term2_between",
    "within_event_var": "term2_within"
})

# -------------------------
# Term 2 = between + within
# -------------------------
df["term2_total"] = df["term2_between"] + df["term2_within"]

# -------------------------
# Relative contributions (Term 2 only)
# -------------------------
df["between_pct"] = 100 * df["term2_between"] / df["term2_total"]
df["within_pct"] = 100 * df["term2_within"] / df["term2_total"]

# -------------------------
# Sanity check: no NaNs or negatives
# -------------------------
assert np.all(df["term2_total"] >= 0), "Negative variance detected!"

# -------------------------
# Output table
# -------------------------
print("\n========== TERM 2 DECOMPOSITION ==========")
print(df[[
    "IM",
    "term2_between",
    "term2_within",
    "term2_total",
    "between_pct",
    "within_pct"
]].to_string(index=False))

# -------------------------
# Invariance check (important theory check)
# -------------------------
vals = df["term2_total"].values
rel_diff = (vals.max() - vals.min()) / vals.mean() * 100

print(f"\nMax relative difference in Term 2 across IMs: {rel_diff:.2f}%")

# -------------------------
# Detailed print (aligned with your equations)
# -------------------------
print("\n========== DETAILED BREAKDOWN ==========")

for _, row in df.iterrows():
    print(f"\nIM: {row['IM']}")
    print(f"(tau^2)*(sum s_i)^2           : {row['term2_between']:.4e} ({row['between_pct']:.1f}%)")
    print(f"(phi^2)*ΣΣ s_i s_k ρ(h_ik)    : {row['term2_within']:.4e} ({row['within_pct']:.1f}%)")
    print(f"Term 2 total                  : {row['term2_total']:.4e}")
    print(f"rho_bar                       : {row['rho_bar']:.6f}")
    print(f"phi^2 * rho_bar               : {row['phi2_rhobar']:.6f}")

# -------------------------
# Save results
# -------------------------
df.to_csv(path / "term2_decomposition.csv", index=False)
