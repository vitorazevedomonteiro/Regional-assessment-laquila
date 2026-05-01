import pandas as pd
from pathlib import Path

# --- Paths ---
path = Path(__file__).parent

gmf = pd.read_csv(path / "GMM_results.csv")
site_model = pd.read_csv(
    path.parent / "GroundMotionFields/job_files/Buildings.csv"
)

# --- Debug: check unique coordinates ---
print("GMF unique coords:", gmf[["lon", "lat"]].drop_duplicates().shape)
print("Site_model unique coords:", site_model[["lon", "lat"]].drop_duplicates().shape)

# --- Step 1: fix floating point precision ---
gmf["lon"] = gmf["lon"].round(5)
gmf["lat"] = gmf["lat"].round(5)

site_model["lon"] = site_model["lon"].round(5)
site_model["lat"] = site_model["lat"].round(5)

# --- Step 2: create a robust key (prevents float mismatch issues) ---
gmf["coord_key"] = gmf["lon"].astype(str) + "_" + gmf["lat"].astype(str)
site_model["coord_key"] = site_model["lon"].astype(str) + "_" + site_model["lat"].astype(str)

# --- Step 3: ensure gmf has unique coordinates (should already be true, but safe) ---
gmf = gmf.drop_duplicates(subset="coord_key")

# --- Step 4: debug matching BEFORE merge ---
matches = site_model.merge(gmf, on="coord_key", how="inner")
print("Matching rows (should be ~1916):", len(matches))

# --- Step 5: merge (this expands to 2962 rows correctly) ---
final = site_model.merge(
    gmf.drop(columns=["lon", "lat"]),  # avoid duplicate columns
    on="coord_key",
    how="left"
)

# --- Step 6: clean up helper column ---
final.drop(columns=["coord_key"], inplace=True)

# --- Step 7: add Building column if missing ---
if "Building" not in final.columns:
    final.insert(0, "Building", [f"Building_{i+1}" for i in range(len(final))])

# --- Step 8: save ---
out_file = path / "GMM_results_expanded.csv"
final.to_csv(out_file, index=False)

print(f"Done! File saved as {out_file}")