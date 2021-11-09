# UpliftModelingWithNRABias

This repository contains the code of the paper : "Evaluation de l'uplift sur des données biaisées dans le cas du Non-Random Assignment"

You can find the code used to 1- generate biased samples     2- Treatment group reweighting with the class transformation approach and the 2 Model approach

To execute the bias generation process with a dataset:

1- The treatment and output columns should be binary (0 and 1) named respectiveley : 'segment' and 'visit'
2- Datasets should be discretized

You can launch the process with the following command:

ipython BiasGenAndReweighting.py DatasetFileName UpliftMethod X NoDA VAR_Name    (For the bias generation process without domain adaptation for samples reweighting)

ipython BiasGenAndReweighting.py DatasetFileName UpliftMethod X rg VAR_Name      (For the bias generation process with the reweighting method "Ratio of gaussians")

For the Uplift method, you can use : 
1- KL 
2- CTS 
3- Chi 
4- ED
5- 2MLR (Two Model Approach with Logistic Regression)
6- 2M_Xgboost (Two Model Approach with Xgboost)
7- CT_Xgboost (Class Transformation Approach with Xgboost)
8- Class Transformation (Class Transformation with Logistic Regression) 
