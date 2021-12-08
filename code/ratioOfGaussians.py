import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import OrdinalEncoder
import seaborn as sns
import numpy as np
from random import seed
from random import randint
from random import gauss
from random import uniform
from random import shuffle
import matplotlib.pyplot as plt
sns.set_style('darkgrid')
get_ipython().run_line_magic('matplotlib', 'inline')
# %matplotlib qt5
from sklearn.model_selection import train_test_split
import hashlib
import random
# random.seed(6)
from IPython.display import Image
from causalml.inference.tree import UpliftTreeClassifier, UpliftRandomForestClassifier
from causalml.inference.tree import uplift_tree_string, uplift_tree_plot
from causalml.metrics import plot_gain
from causalml.metrics import get_qini
from causalml.metrics import plot_qini
from causalml.metrics import qini_score
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
from itertools import combinations 
import os
import sys
random.seed(7)
from sklift.metrics import (
    uplift_at_k, uplift_auc_score, qini_auc_score, weighted_average_uplift
)
from sklift.models import TwoModels
from sklearn.linear_model import LogisticRegression
from sklift.models import ClassTransformation
from catboost import CatBoostClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
import sys
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
import scipy.stats as st
from scipy.linalg import eig, eigh, svd
from scipy.spatial.distance import pdist, squareform
import adapt
from adapt.instance_based import KLIEP
from sklearn.tree import DecisionTreeRegressor
from sklearn.decomposition import PCA
from sklearn.svm import LinearSVC, SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV, \
    RidgeClassifier, RidgeClassifierCV
from sklearn.model_selection import cross_val_predict
from sklearn.calibration import CalibratedClassifierCV
from os.path import basename
from scipy.spatial.distance import cdist
from cvxopt import matrix, solvers
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
import numpy as np
import scipy.stats as st
from scipy.sparse.linalg import eigs
from scipy.spatial.distance import cdist
import sklearn as sk
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV, \
    RidgeClassifier, RidgeClassifierCV
from sklearn.model_selection import cross_val_predict
from os.path import basename
import ot
from sklearn.preprocessing import MinMaxScaler


def is_pos_def(X):
    """Check for positive definiteness."""
    print("Check for pos def")
    print(X)
    return np.all(np.linalg.eigvals(X) > 0)

def iwe_ratio_gaussians(X, Z):
        """
        Estimate importance weights based on a ratio of Gaussian distributions.
        Parameters
        ----------
        X : array
            source data (N samples by D features)
        Z : array
            target data (M samples by D features)
        Returns
        -------
        iw : array
            importance weights (N samples by 1)
        """
        print("X in rg is ")
        print(X)
        # Data shapes
        N, DX = X.shape
        M, DZ = Z.shape

        # Assert equivalent dimensionalities
        if not DX == DZ:
            raise ValueError('Dimensionalities of X and Z should be equal.')

        # Sample means in each domain
        mu_X = np.mean(X, axis=0)
        mu_Z = np.mean(Z, axis=0)

        # Sample covariances
        Si_X = np.cov(X.T)
        Si_Z = np.cov(Z.T)

        # Check for positive-definiteness of covariance matrices
        if not (is_pos_def(Si_X) or is_pos_def(Si_Z)):
            print('Warning: covariate matrices not PSD.')

            regct = -2
            while not (is_pos_def(Si_X) or is_pos_def(Si_Z)):
                print('Adding regularization: ' + str(1**regct))

                # Add regularization
                Si_X += np.eye(DX)*10.**regct
                Si_Z += np.eye(DZ)*10.**regct

                # Increment regularization counter
                regct += 1

        pT = st.multivariate_normal.pdf(X, mu_Z, Si_Z,allow_singular=True)
        pS = st.multivariate_normal.pdf(X, mu_X, Si_X,allow_singular=True)
        
        print("pT nan values ",np.any(np.isnan(pS)))
        print("pT 0 values ",pS)
        print("pT 0 values ",np.any(pS == 0))
        pS[pS==0]=0.00001
        # Check for numerical problems
        if np.any(np.isnan(pT)) or np.any(pT == 0):
#             raise ValueError('Source probabilities are NaN or 0.')
            print("Source probabilities are NaN or 0")
        if np.any(np.isnan(pS)) or np.any(pS == 0):
            raise ValueError('Source probabilities are NaN or 0.')

        # Return the ratio of probabilities
        weight_to_return=(pT / pS)# * (pT / 1-pS)
        iw=weight_to_return
        iw = np.minimum(15, np.maximum(0.8, weight_to_return))
        
#         scaler = MinMaxScaler(feature_range=(0,100))
#         scaled = scaler.fit_transform(weight_to_return.reshape(-1, 1))
#         return scaled[:,0]
        return iw
