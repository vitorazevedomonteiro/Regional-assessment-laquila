# Regional_assessment_laquila
To run MSA:
  1. Go to folder called "3Dbuildings_cdl_1h" 
  2. The data folder should contain a folder called "MSA-Records_0.33_dp04", which should have inside folder regarding the IMs and the POEs selected like: "records_SA(0.33)_0.1", "records_Sa_avg2(0.33)_0.3", "records_FIV3(0.33)_0.9", etc
  3. The output folder is the folder that will contain the outputs from the analysis chosen
  4. I used the python script run_msa_mp.py to run MSA in this specific building typology.
    4.1. Do not forget that since I want the code to run this model specifically I need to change the following scripts to read the models that exist inside the folder src/vitor_3Dbuildings:
      - msa.py
      - rcmrf.py
      - utilities.py
    In these scripts I only changed from where I was calling the models: 'from .vitor_3Dbuildings.CR_LFINF_7_CDL_1H_dp04.model import build_model'