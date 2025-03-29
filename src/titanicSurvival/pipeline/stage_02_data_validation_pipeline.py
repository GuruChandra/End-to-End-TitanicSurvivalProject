import os
import urllib.request as request
import zipfile
from titanicSurvival.logging import logger
from titanicSurvival.components.data_validation import DataValidation
from titanicSurvival.config.configuration import ConfigurationManager

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
       try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation()
            datavalidation = DataValidation(config=data_validation_config)
            datavalidation.validate_files_exist()
       except Exception as e:
            raise e
