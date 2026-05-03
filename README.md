# Regional assessment laquila
To run MSA:
  1. Go to folder called "3Dbuildings" 
  2. The data folder should contain a folder called "cloud", which should have inside folder regarding the record sets like: "set1", "set2", etc.
  3. The output folder is the folder that will contain the outputs from the analysis chosen
  4. I used the python script run_msa_mp.py to run MSA in this specific building typology. You should set taxonomy and record_set parameters, e.g., taxonomy = "CR_LFINF_7_CDL_4H_dp04" and record_set = "cloud".
  5. Outputs are named after taxonomy and folder names for each subset of records (e.g., set1, and set2).

About Section 8:
  1. 'Term1.py' corresponds to Equation 39, which demonstrates the part of the variance of the loss that comes from aleatory uncertainty in Damage States definition
  2. 'Term2.py' corresponds to Equation 47, which is decomposed into two parts. The first part is the between-event contribution and the second part is the within-event contribution.
    2.1 There is the python script "LossWithinVariability.py" that stores all the information from the within-event variability (phi), spatial correlation between the different periods analysed in that formula 47, and the loss sensitivity of the IMs (names as 'si').
    2.2 There is the python script "LossWithinVariability.py" that stores all the information from the between-event variability (tau), and also the loss sensistivity of the IMs.
    2.3. Just to note that those two previous scripts in 2.1 and 2.2 call the "loss_sensitivity_{im_name}.csv", and "Building_Pair_Correlations_{im_name}.csv" which are not in this repository but I have the files.
  3. 'Get_si.py' is the python script that calculates and creates the csv files for the loss sensitivity of the analysed IMs.
  4. 'Mechanism3.py' corresponds to Equations 50 and 51.
  5. 'EmpiricalVariance.py' as the name sugests, calculates the empirical variance of the losses, and stores the results in a csv file, and it's that information that helps to build Table 5.