from titanicSurvival.logging import logger
from titanicSurvival.entity import ModelTrainerConfig
from titanicSurvival.config.configuration import ConfigurationManager
from titanicSurvival.components.data_transformation import getAgeSubSection, assignCabin
import joblib
from pathlib import Path
import os
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_trainer()
        
    def convert_input_data_exp_feature_vector(self,input_data):
        df  = input_data#pd.DataFrame(input_data)
        df['Sex'] = df['Sex'].fillna(df['Sex'].mode()[0]).map({'female':0, 'male': 1 })
        df['Age']=df['Age'].fillna(df['Age'].mode()[0])
        df['Age']=df['Age'].apply(lambda x: getAgeSubSection(x))
        df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0])
        df['Embarked'] = (df['Embarked'].map({'C':0, 'S':1, 'Q':2})).astype(int)
        
        df['Cabin']=df['Cabin'].fillna("X").map(lambda x: x[0])
        df['Cabin']=df.apply(lambda row: assignCabin(row),axis=1)
        print(f"Cabin data after assigned values: {df['Cabin'].head()}")

        cabinEncode = OrdinalEncoder()
        df['Cabin']=(cabinEncode.fit_transform(df[['Cabin']])).astype(int)
        df.drop(columns=['PassengerId','Name','Ticket','Fare'],inplace=True,axis=1)
        #print(df['Cabin'].isnull().sum())
        print(df.head())
        df_np = df.to_numpy()
        return df_np



    def predit(self,input_data):
        model = joblib.load(os.path.join(self.config.root_dir,'model.pkl'))
        input_feature= self.convert_input_data_exp_feature_vector(input_data)
        predicted_out =model.predict(input_feature)
        logger.info(f"Input Data: {input_data}")
        logger.info(f"Predicted Output: {predicted_out}")
        return predicted_out