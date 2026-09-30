# Regional seismic risk assessment using several intensity measures, different correlation modelling approaches, and record sets.

The study evaluates how the spatial and IM-correlation modelling choices, selection of intensity measures (IMs), and ground motion record datasets affects the fragility and loss estimates used in regional loss assessment for a heterogeneous portfolio of buildings. It compares traditional IMs (PGA and Sa(T)) against next-generation IMs (Saavg(T) and FIV3(T)), across a range of vibration periods and two record-selection datasets.

This repository contains the data, structural models, and results supporting the papers presented below.

## Reference

V. A. Monteiro, V. Ozsarac, D. Shahnazaryan, and G. J. O'Reilly, "Spatial correlation modelling strategies and intensity measure choices in regional seismic loss assessment" (under review), 2026.

V. A. Monteiro and G. J. O'Reilly, "Record selection effects on aggregate loss estimates for regional seismic portfolios" (under review), 2026.

## Study parameters

The analyses span the following dimensions, which recur throughout the folder structure:

- **Intensity Measures (IMs):** PGA, Sa(T), Saavg(T), and FIV3(T)
- **Periods (T):** 0.14, 0.33, 0.45, 0.7, 1.5 s
- **Record datasets:**
  - `CS_dataset` — records selected using Conditional Spectrum (CS) record selection
  - `FEMAP695` — records from the FEMA-P695 far-field set
- **Building typologies:** the suite of buildings analysed in the study (see `SimDesignModels`). Briefly, these are reinforced concrete buildings from 1 to 4 storeys, considering low-code and medium-code levels.

## SimDesignModels

The OpenSeesPy models for every building used in the study. These are the numerical models on which all subsequent analyses are based.

## 3Dbuildings

The setup used to run Multiple Stripe Analysis (MSA) on the buildings. This is where the structural models are subjected to the ground-motion records across increasing intensity levels.

## Fragility_functions

Fragility functions derived for all buildings, IMs, periods, and both record datasets. Figures of the fragility curves are organised into two subfolders by record dataset:

- `CS_dataset` — fragility curves obtained under Conditional Spectrum record selection
- `FEMAP695` — fragility curves obtained using FEMA P-695 far-field records

The file `fragility_parameters.pdf` collects, in one place, the fitted parameters of every fragility function, for all IMs, periods, typologies, and record datasets.

## HazardConsistencyPlots

Hazard consistency checks for several buildings. These plots verify whether the selected records (CS-based or FEMA P-695) reproduce the target site hazard.

## LossDistributionTypologies

Disaggregation of the expected losses across the different damage states and across the different building typologies, presented for all IMs and periods.
