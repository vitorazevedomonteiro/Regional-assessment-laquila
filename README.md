# Regional_assessment_laquila
To run MSA:
  1. Go to folder called "3Dbuildings" 
  2. The data folder should contain a folder called "cloud", which should have inside folder regarding the record sets like: "set1", "set2", etc.
  3. The output folder is the folder that will contain the outputs from the analysis chosen
  4. I used the python script run_msa_mp.py to run MSA in this specific building typology. You should set taxonomy and record_set parameters, e.g., taxonomy = "CR_LFINF_7_CDL_4H_dp04" and record_set = "cloud".
  5. Outputs are named after taxonomy and folder names for each subset of records (e.g., set1, and set2).