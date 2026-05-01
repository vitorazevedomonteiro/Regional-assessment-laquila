import pandas as pd
import numpy as np
import json
from pathlib import Path
from scipy.stats import norm

path = Path(__file__).parent

imt = 'PGA'

# -------------------------
# Load IM values (η)
# -------------------------
im_df = pd.read_csv(
    path.parent
    / "GroundMotionFields/final_files"
    / f"gmf_{imt}_openquake_MAO2026_RandomSeed_50_mw6.3.csv"
)

# assume column name is IM_sim0
eta_values = im_df["IM_sim0"].values  # shape (N,)

# -------------------------
# Replacement costs
# -------------------------
repl_cost_file = pd.read_csv(
    path.parent / "GroundMotionFields/repl_cost.csv"
)

tax_to_repl = {
    row["TAXONOMY"].strip(): float(row["REPL_COST_BUILD_NONSTRUC_STRUCT"])
    for _, row in repl_cost_file.iterrows()
}

# -------------------------
# Taxonomy assignment
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

# build arrays aligned with eta
N = len(eta_values)
taxonomy_array = np.empty(N, dtype=object)

for tax, rng in tax_seq:
    for i in rng:
        taxonomy_array[i - 1] = tax  # assuming Building_1 → index 0

# -------------------------
# Load fragility per taxonomy
# -------------------------


def load_fragility_json(tax):
    if imt == 'PGA':
        json_fp = (
            path.parent
            / "outputs"
            / "MSA"
            / f"{tax}_dp04"
            / "frags_msa_SA(0.01).json"
        )
    else:
        json_fp = (
            path.parent
            / "outputs"
            / "MSA"
            / f"{tax}_dp04"
            / f"frags_msa_{imt}.json"
        )

    medians = np.zeros(4)
    betas = np.zeros(4)

    with open(json_fp, "r") as f:
        frag_data = json.load(f)

    for k, dls in enumerate(["DLS-1", "DLS-2", "DLS-3", "DLS-4"]):
        medians[k] = frag_data[dls]["median"]
        betas[k] = frag_data[dls]["beta"]

    return medians, betas

# cache fragilities


fragility = {}
for tax, _ in tax_seq:
    fragility[tax] = {}
    theta, beta = load_fragility_json(tax)
    fragility[tax]["theta"] = theta
    fragility[tax]["beta"] = beta

# -------------------------
# Damage ratios (include DS0!)
# -------------------------
dam_ratio_file = pd.read_csv(path.parent / "GroundMotionFields/Dam_ratio.csv")

DR = np.array([0.0] + [
    dam_ratio_file.loc[dam_ratio_file["Dstates"] == f"DS{i}", "DR"].iloc[0]
    for i in range(1, 5)
])

# -------------------------
# Fragility → DS probabilities
# -------------------------


def get_ds_probabilities(eta, theta, beta):

    P_exceed = norm.cdf((np.log(eta) - np.log(theta)) / beta)

    probs = np.zeros(5)

    probs[0] = 1 - P_exceed[0]
    probs[1] = P_exceed[0] - P_exceed[1]
    probs[2] = P_exceed[1] - P_exceed[2]
    probs[3] = P_exceed[2] - P_exceed[3]
    probs[4] = P_exceed[3]

    return probs

# -------------------------
# Compute Term 1
# -------------------------


term1 = 0.0

for i in range(N):

    eta = eta_values[i]
    tax = taxonomy_array[i]

    if np.isnan(eta):
        continue

    theta = fragility[tax]["theta"]
    beta = fragility[tax]["beta"]

    probs = get_ds_probabilities(eta, theta, beta)

    E_DR = np.dot(DR, probs)
    E_DR2 = np.dot(DR**2, probs)

    var_DR = E_DR2 - E_DR**2

    Ci = tax_to_repl[tax]

    term1 += (Ci ** 2) * var_DR

print(f"\n=== Term 1 (fragility-based) for {imt} ===")
print(term1)
