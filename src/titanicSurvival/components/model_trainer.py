import os
import urllib.request as request
import zipfile
from titanicSurvival.logging import logger
from titanicSurvival.utils.common import get_size
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import classification_report
from typing import Any
from sklearn.linear_model import LogisticRegression
import joblib
from titanicSurvival.entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config =config
    
    def get_transformed_data(self) -> tuple[np.array, np.array, np.array, np.array]:
        try:
            X_train_df = pd.read_csv(os.path.join('artifacts/data_transformation/','train_features_x.csv'))
            y_train_df = pd.read_csv(os.path.join('artifacts/data_transformation/','train_features_y.csv'))
            X_test_df = pd.read_csv(os.path.join('artifacts/data_transformation/','test_features_x.csv'))
            y_test_df = pd.read_csv(os.path.join('artifacts/data_transformation/','test_features_y.csv'))
            
            logger.info(f"Cocatenated train and test data")
            print(X_train_df.head())
            return X_train_df.to_numpy(),y_train_df.to_numpy(),X_test_df.to_numpy(),y_test_df.to_numpy()
        except Exception as e:
            raise e
    
    
    def fit_model(self,X_train,y_train,X_test,y_test):

        X_train, y_train, X_test, y_test = self.get_transformed_data()

        lr = LogisticRegression()

        lr.fit(X_train,y_train)
        logger.info(f"{ classification_report(y_test,lr.predict(X_test))}")

        joblib.dump(lr,os.path.join(self.config.root_dir,'model.pkl'))
        logger.info(f"Model Save to path: {self.config.root_dir}")

            
