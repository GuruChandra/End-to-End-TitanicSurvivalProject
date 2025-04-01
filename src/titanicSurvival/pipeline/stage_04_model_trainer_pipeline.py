import os
import urllib.request as request
import zipfile
from titanicSurvival.logging import logger
from titanicSurvival.components.model_trainer import ModelTrainer
from titanicSurvival.config.configuration import ConfigurationManager

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            modletrainer_config = config.get_model_trainer()
            model_trainer=ModelTrainer(config=modletrainer_config)
            X_train,y_train,X_test,y_test =model_trainer.get_transformed_data()
            model_trainer.fit_model(X_train,y_train,X_test,y_test)
            
        except Exception as e:
            raise e