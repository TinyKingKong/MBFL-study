# MBFL-study
This repository contains source code in our study paper "A Systematic Exploration of Mutation-Based Fault Localization Formulae"

The main experiment results can be reproduced by the scripts under the folder `eval`.

Here are the usefull files:
```
|-- MBFL-study
    |-- eval/
        |-- method_level_result_show.py    ## The entrance for calculating the method level reseults
        |-- result_show.py    ## The entrance of BLMu
        |-- spectrum_result_show.py    ## The entrance of the MBFL formulae transformed from SBFL
    |-- preprocess/    ## The preprocessor for Defects4J data
    |-- spectrum_based
        |-- sbfl.py    ## The calculator for SBFL
        |-- get_top_n_method.py    ## The results for method level of SBFL formulae
        |-- get_top_n_stmt.py    ## The result for statement level of SBFL formulae
```
