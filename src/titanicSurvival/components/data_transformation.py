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
from titanicSurvival.entity import DataTransformationConfig


def getAgeSubSection(age):
    #print(age)
    if age > 60:
        return 5
    elif age > 50:
        return 4
    elif age > 40:
        return 3
    elif age > 30:
        return 2
    #elif age > 20:
    #   return 2
    elif age > 15:
        return 1
    else:
        return 0
def assignCabin(row):
    if row.Cabin == 'X':
        if row.Pclass == 1 :
            return 'C'
        elif row.Pclass == 2:
            return 'F'
        else:
            return 'G'
    else:
        return row.Cabin
    

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config =config

    def combine_train_test_data(self):
        try:
            df = pd.read_csv(os.path.join('artifacts/data_ingestion/','train.csv'))
            target_df = pd.read_csv(os.path.join('artifacts/data_ingestion/','gender_submission.csv'))
            test_df = pd.read_csv(os.path.join('artifacts/data_ingestion/','test.csv'))
            test_df.insert(1,'Survived',target_df['Survived'])
            df = pd.concat([df, test_df])
            logger.info(f"Cocatenated train and test data")
            return df
        except Exception as e:
            raise e


    def create_features(self):

        df = self.combine_train_test_data()
        
        df['Sex'] = df['Sex'].fillna(df['Sex'].mode()[0]).map({'female':0, 'male': 1 })
        df['Age']=df['Age'].fillna(df['Age'].mode()[0])
        df['Age']=df['Age'].apply(lambda x: getAgeSubSection(x))
        df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0])
        df['Embarked'] = (df['Embarked'].map({'C':0, 'S':1, 'Q':2})).astype(int)
        
        df['Cabin']=df.apply(lambda row: assignCabin(row),axis=1)


        cabinEncode = OrdinalEncoder()
        df['Cabin']=(cabinEncode.fit_transform(df[['Cabin']])).astype(int)
        #print(df['Cabin'].isnull().sum())
        df_np = df.to_numpy()

        X_train,y_train = df_np[:-418,1:],df_np[:-418,0]
        X_test,y_test = df_np[-418:,1:],df_np[-418:,0]

        X_train_path = os.path.join(self.config.root_dir, 'train_features_x.csv')
        pd.DataFrame(X_train).to_csv(X_train_path,index=False)

        y_train_path = os.path.join(self.config.root_dir, 'train_features_y.csv')
        pd.DataFrame(y_train).to_csv(y_train_path,index=False)

        logger.info(f"Train feature files created: {X_train_path} \n and {y_train_path}")
        X_test_path = os.path.join(self.config.root_dir, 'test_features_x.csv')
        pd.DataFrame(X_test).to_csv(X_test_path,index=False)

        y_test_path = os.path.join(self.config.root_dir, 'test_features_y.csv')
        pd.DataFrame(y_test).to_csv(y_test_path,index=False)
        logger.info(f"Test feature files created: {X_test_path} \n and {y_test_path}")


        
