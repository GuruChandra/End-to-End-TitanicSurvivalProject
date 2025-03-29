import os
import urllib.request as request
import zipfile
from titanicSurvival.logging import logger
from titanicSurvival.components.data_transformation import DataTransformation
from titanicSurvival.config.configuration import ConfigurationManager

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            dat_transforamtion_config = config.get_data_transformation()
            data_transformation = DataTransformation(config=dat_transforamtion_config)
            data_transformation.create_features()
        except Exception as e:
            raise e
