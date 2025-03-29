import os
import urllib.request as request
import zipfile
from titanicSurvival.logging import logger
from titanicSurvival.utils.common import get_size
from titanicSurvival.entity import DataValidatioConfig


class DataValidation:
    def __init__(self,config:DataValidatioConfig):
        self.config =config
    
    def validate_files_exist(self) -> bool:
        try:
            for file in self.config.ALL_REQUIRED_FILES:
                if os.path.exists(os.path.join('artifacts/data_ingestion',file)):
                    with open(self.config.status_file, 'w') as fp:
                        fp.write(f'File exising: {file}')
                    logger.info(f"File Existing: {file}")
                    validation_status = True
                else:
                    with open(self.config.status_file, 'w') as fp:
                        fp.write(f'File Not exising: {file}')
                    validation_status = False

                    logger.info(f"File Not Existing: {file}")
            return validation_status
        except Exception  as e:
            raise e