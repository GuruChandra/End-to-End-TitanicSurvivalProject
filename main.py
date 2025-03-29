from titanicSurvival.logging import logger
from titanicSurvival.pipeline.stage_01_dataingestion_pipeline import DataIngestionPipeline


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
