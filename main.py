from PoultryDiseaseClassificationCNN import logger
from PoultryDiseaseClassificationCNN.components.data_ingestion_compo import DataIngestion
from PoultryDiseaseClassificationCNN.pipeline.data_inge_pipeline_o1 import  DataIngestionPipeline

STAGE_NAME = "Data_ingestion"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
