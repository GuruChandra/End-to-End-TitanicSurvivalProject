import os
from pathlib import Path
import urllib.request as request
import zipfile
from titanicSurvival.logging import logger
from titanicSurvival.utils.common import get_size
from titanicSurvival.config.configuration import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config =config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n {headers}")
        else:
            logger.info(f"File already exists with size: {get_size(Path(self.config.local_data_file))}")

    
    def extract_zip_file(self):
        os.makedirs(self.config.unzip_dir,exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file) as zf:
            zf.extractall(self.config.unzip_dir)