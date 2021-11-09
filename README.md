# UpliftModelingWithNRABias

## This repository contains the code of the paper : "Evaluation de l'uplift sur des données biaisées dans le cas du Non-Random Assignment"

You can find the code used to 1- generate biased samples     2- Treatment group reweighting with the class transformation approach and the 2 Model approach

To execute the bias generation process with a dataset:

1- The treatment and output columns should be binary (0 and 1) and named respectively : 'segment' and 'visit' <br />
2- Datasets should be discretized <br />

You can launch the process with the following command on a Linux machine:

#### (For the bias generation process without domain adaptation for samples reweighting): <br />

*ipython BiasGenAndReweighting.py DatasetFileName UpliftMethod X NoDA VAR_Name*    

#### (For the bias generation process with the reweighting method "Ratio of gaussians"): <br />
*ipython BiasGenAndReweighting.py DatasetFileName UpliftMethod X rg VAR_Name* 

#### For the Uplift methods, you can use :  <br />
1- KL <br />
2- CTS <br />
3- Chi <br />
4- ED <br />
5- 2MLR (Two Model Approach with Logistic Regression) <br />
6- 2M_Xgboost (Two Model Approach with Xgboost) <br />
7- CT_Xgboost (Class Transformation Approach with Xgboost) <br />
8- Class Transformation (Class Transformation with Logistic Regression) <br />

## Following is some of the results of the benchmark that demonstrates the behavior of several uplift methods when facing NRA bias :
<p float="left">
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/Criteo_f2.png" width="310" />
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/Criteo_f2'.png" width="310" /> 
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/Criteo_f8'.png" width="310" />
</p>

<p float="left">
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/Criteo_f8'.png" width="310" />
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/Gerber_p2002'.png" width="310" /> 
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/Gerber_p2004'.png " width="310" />
</p>

<p float="left">
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/Gerber_p2004.png " width="310" />
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/Hillstrom_mens'.png" width="310" /> 
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/Hillstrom_mens.png" width="310" />
</p>

<p float="left">
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/Hillstrom_newbie'.png" width="310" />
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/Hillstrom_newbie.png" width="310" /> 
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/Synth2'.png" width="310" />
</p>

<p float="left">
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/Synth2.png" width="310" />
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/megafone_X16'.png" width="310" /> 
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/megafone_X16.png" width="310" />
</p>

<p float="left">
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/megafone_X21'.png" width="310" />
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/megafone_X21.png" width="310" /> 
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/retailHero_age'.png" width="310" />
</p>

<p float="left">
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/retailHero_age.png" width="310" />
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/retailHero_trNum'.png" width="310" /> 
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/retailHero_trNum.png " width="310" />
</p>

<p float="left">
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/verysmallRateYNoisyv2__Comb2.png" width="310" />
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/verysmallRateYNoisyv2_prime_Comb2.png" width="310" /> 
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/zenodoSynth_X10'.png" width="310" />
</p>
<p float="left">
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/zenodoSynth_X10.png" width="310" />
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/zenodoSynth_X31'.png" width="310" /> 
  <img src="https://github.com/MinaWagdi/UpliftModelingWithNRABias/blob/main/FigResults/Figs/zenodoSynth_X31.png" width="310" />
</p>

Following is the table of the results 

| {}                 | 2M_Xgboost         | CT_Xgboost | 2M_LR               | CT_LR | KL                  | ED                  | CTS       | Chi                 |
|--------------------|---------------------|-------------|--------------------|---------------------|---------------------|---------------------|-----------|---------------------|
| Criteo\_f2         | 6.6(1.7)            | 0.2(1.9)    | **7.2(1.6)** | 1.9(1.2)            | 0.6(1.4)            | 4.9(1.3)            | 2.1(1.5)  | -2.1(1.6)           |
| Criteo\_f2'        | 6.4(2.7)            | 6.9(2.0)    | 10.1(1.4)          | 7.6(1.4)            | 10.3(1.2)           | **11.0(1.2)** | 10.5(1.3) | 10.1(1.3)           |
| Criteo\_f8         | **8.1(2.6)**  | 0.1(1.7)    | 6.3(2.0)           | 1.7(1.0)            | 1.2(1.6)            | 5.2(1.2)            | 2.4(1.6)  | -1.4(1.6)           |
| Criteo\_f8'        | **7.2(2.6)**  | -2.5(1.7)   | 7.1(2.2)           | -2.0(1.3)           | -1.3(1.5)           | 4.5(1.6)            | 2.3(1.9)  | -1.9(1.7)           |
| Gerber\_p2002      | -2.4(2.0)           | -2.1(1.5)   | **1.1(1.1)** | -0.4(1.2)           | -1.5(1.8)           | -0.9(1.5)           | -0.1(1.7) | -1.5(1.8)           |
| Gerber\_p2002'     | -2.4(1.9)           | -1.5(2.2)   | 0.6(1.1)           | **1.0(1.1)**  | -0.8(1.6)           | -0.4(1.6)           | 0.1(1.6)  | -0.8(1.7)           |
| Gerber\_p2004      | -2.1(2.0)           | -1.8(1.7)   | **0.8(1.1)** | -1.2(1.3)           | -1.7(1.8)           | -1.5(1.9)           | -0.6(1.9) | -1.9(1.8)           |
| Gerber\_p2004'     | -2.4(2.0)           | -1.1(2.4)   | 1.0(1.3)           | **1.4(1.4)  | -1.3(1.3)           | -0.9(1.4)           | 0.0(1.5)  | -1.3(1.3)           |
| Hillstrom\_mens    | 2.7(2.1)            | -4.1(2.0)   | **5.5(2.6)** | -4.6(2.2)           | 2.8(2.6)            | 2.9(2.5)            | 1.0(2.8)  | 2.8(2.6)            |
| Hillstrom\_mens'   | 2.7(2.5)            | 4.6(1.5)    | 6.5(2.7)           | **6.6(1.9)**  | 4.8(2.5)            | 4.9(2.1)            | 6.0(2.1)  | 4.8(2.3)            |
| Hillstrom\_newbie  | 2.8(2.2)            | 0.1(2.1)    | **6.2(2.7)** | 2.4(1.9)            | 4.2(2.2)            | 4.3(2.5)            | 4.3(2.5)  | 4.1(2.4)            |
| Hillstrom\_newbie' | 3.6(2.6)            | 1.7(2.1)    | **6.2(2.2)** | 4.1(1.9)            | 4.7(1.9)            | 4.8(2.0)            | 4.9(2.3)  | 4.6(2.0)            |
| Megafone\_X16      | **17.8(0.5)** | 8.6(0.6)    | 3.5(0.4)           | 3.2(0.4)            | 13.2(0.5)           | 13.7(0.5)           | 11.6(0.7) | 13.2(0.4)           |
| Megafone\_X16'     | **18.0(0.4)** | 14.2(0.5)   | 3.6(0.4)           | 3.1(0.5)            | 13.5(0.5)           | 13.7(0.5)           | 12.2(0.6) | 13.4(0.6)           |
| Megafone\_X21      | **18.2(0.4)** | 12.0(0.4)   | 3.5(0.4)           | 2.4(0.5)            | 13.9(0.5)           | 14.0(0.6)           | 10.7(0.8) | 13.7(0.5)           |
| Megafone\_X21'     | **18.2(0.5)** | 12.8(0.4)   | 3.3(0.6)           | 1.8(0.6)            | 13.6(0.5)           | 13.9(0.5)           | 11.9(0.6) | 13.5(0.5)           |
| Synth1             | 7.0(0.9)            | 1.7(0.9)    | 0.9(1.6)           | -2.9(1.3)           | **9.7(1.2)**  | 8.8(1.6)            | 8.7(1.2)  | 9.6(1.8)            |
| Synth1'            | 9.5(1.5)            | -0.4(3.0)   | 2.1(0.7)           | -0.8(2.8)           | 12.0(1.9)           | 11.1(2.3)           | 10.4(1.8) | **12.5(1.9)** |
| Synth2             | 9.8(0.1)            | 8.1(0.5)    | 1.9(0.1)           | 1.1(0.2)            | 9.7(0.1)            | 9.6(0.2)            | 8.7(0.1)  | **9.9(0.2)**  |
| Synth2'            | **10.0(0.1)** | 8.6(0.1)    | 1.7(0.0)           | 1.4(0.4)            | 9.8(0.1)            | 9.5(0.2)            | 8.8(0.2)  | 9.9(0.1)            |
| retailHero\_age    | 0.7(0.4)            | 0.3(0.4)    | **1.2(0.3)** | 0.8(0.4)            | 0.8(0.3)            | 0.9(0.3)            | 0.9(0.4)  | 0.9(0.3)            |
| retailHero\_age'   | 0.7(0.5)            | 0.6(0.4)    | 1.2(0.3)           | **1.3(0.4)**  | 0.9(0.4)            | 0.9(0.4)            | 0.6(0.5)  | 0.9(0.4)            |
| retailHero\_trNum  | 0.8(0.4)            | 0.4(0.3)    | **1.2(0.3)** | 1.1(0.4)            | 0.7(0.4)            | 0.7(0.4)            | 0.6(0.4)  | 0.7(0.4)            |
| retailHero\_trNum' | 0.8(0.4)            | 0.5(0.4)    | **1.2(0.4)** | 1.1(0.4)            | 0.6(0.4)            | 0.6(0.5)            | 0.3(0.4)  | 0.6(0.4)            |
| zenodoSynth\_X10   | 9.7(1.8)            | 7.0(2.2)    | 12.6(1.9)          | 12.1(1.5)           | 12.8(1.9)           | **13.0(1.9)** | 10.6(2.6) | 12.8(1.8)           |
| zenodoSynth\_X10'  | 9.5(2.1)            | 6.9(2.1)    | 12.6(1.8)          | 12.0(1.7)           | **13.5(2.4)** | **13.5(2.4)** | 10.7(2.5) | 13.3(2.4)           |
| zenodoSynth\_X31   | 9.8(2.4)            | 6.6(2.0)    | 12.2(2.0)          | 12.0(1.9)           | 12.7(1.9)           | **13.2(2.0)** | 10.2(2.2) | 12.8(1.8)           |
| zenodoSynth\_X31'  | 9.5(2.4)            | 9.2(2.0)    | 12.2(1.8)          | 11.8(1.5)           | 13.0(2.5)           | **13.4(2.3)** | 12.1(2.1) | 13.0(2.4)           |
