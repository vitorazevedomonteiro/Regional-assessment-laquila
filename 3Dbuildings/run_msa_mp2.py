import numpy as np
from pathlib import Path
from src.gm_records import get_records
from src.msa_mp import MSA_MP
from src.rcmrf import RCMRF


if __name__ == "__main__":
        
    taxonomy = "CR_LFINF_7_CDL_2H_dp04_q1"
    record_set = "cloud"
    
    path = Path(__file__).parent
    outputs_dir = (
        path
        / f"outputs/{record_set}/{taxonomy}"
    )
    outputs_dir.mkdir(parents=True, exist_ok=True)
    gmdir = path / f"data/{record_set}"
    gmfilenames = ["GMR_filenames_X.txt", "GMR_filenames_Y.txt", "GMR_dts.txt"]

    rcmrf = RCMRF(
        analysis_options=["msa"],
        export_dir=outputs_dir,
        gm_folder=gmdir,
        gm_filenames=gmfilenames,
        taxonomy=taxonomy
    )

    eigenvalues = rcmrf.get_modal_properties()

    records = get_records(gmdir, gmfilenames, outputs_dir)

    msa = MSA_MP(
        analysis_options=["msa"],
        export_dir=outputs_dir,
        gm_folder=gmdir,
        gm_filenames=gmfilenames,
        multiprocess=True,
        damping=eigenvalues["Damping"][0],
        omegas=eigenvalues["CircFreq"],
        # analysis_time_step=0.005,
        taxonomy=taxonomy
    )

    msa.start(records, workers=10)
