from titanicSurvival.logging import logger
from titanicSurvival.pipeline.stage_01_dataingestion_pipeline import DataIngestionPipeline
from titanicSurvival.pipeline.stage_02_data_validation_pipeline import DataValidationPipeline
from titanicSurvival.pipeline.stage_03_data_transformation_pipeline import DataTransformationPipeline
from titanicSurvival.pipeline.stage_04_model_trainer_pipeline import ModelTrainerPipeline
logger.info("Welcome to our custom logging...")


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<< \n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

logger.info(f"X------------------------------------------------------------------X")

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<< \n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

logger.info(f"X------------------------------------------------------------------X")

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<< \n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e


logger.info(f"X------------------------------------------------------------------X")

STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_transformation = ModelTrainerPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<< \n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e


logger.info(f"X------------------------------------------------------------------X")