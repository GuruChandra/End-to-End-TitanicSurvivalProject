import os
import urllib.request as request
import zipfile
from titanicSurvival.logging import logger
from titanicSurvival.components.data_ingestion import DataIngestion
from titanicSurvival.config.configuration import ConfigurationManager

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
       try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
       except Exception as e:
            raise e
