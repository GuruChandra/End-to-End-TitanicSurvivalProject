from titanicSurvival.constants import *
from titanicSurvival.utils.common import  read_yaml, create_directories
from titanicSurvival.entity import DataIngestionConfig,DataValidatioConfig,DataTransformationConfig

class ConfigurationManager:
    def __init__(self,
                 config_file_path= CONFIG_FILE_PATH,
                 params_file_path= PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])
    def get_data_ingestion(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        return data_ingestion_config
    

    def get_data_validation(self) -> DataValidatioConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_valiation_config = DataValidatioConfig(
            root_dir=config.root_dir,
            status_file=config.status_file,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )
        return data_valiation_config
    
    def get_data_transformation(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_tranformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            
        )
        return data_tranformation_config