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


