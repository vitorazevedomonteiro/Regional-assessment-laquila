from pathlib import Path
from src.rcmrf import RCMRF


path = Path(__file__).parent
outputs_dir = (
    path
    / "outputs/IDA/CR_LFINF_7_CDL_1H_dp04"
)
outputs_dir.mkdir(parents=True, exist_ok=True)

gmdir = path / "data/IDA"

gmfilenames = ["GMR_filenames_X.txt", "GMR_filenames_Y.txt", "GMR_dts.txt"]

model = RCMRF(
    analysis_options=["ida"],
    export_dir=outputs_dir,
    gm_folder=gmdir,
    gm_filenames=gmfilenames,
    im_type=2,
    dcap=5,
    analysis_time_step=0.005,
    workers=40
)

model.modeller()
model.wipe()
