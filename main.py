from PoultryDiseaseClassificationCNN import logger
from PoultryDiseaseClassificationCNN.pipeline.data_inge_pipeline_o1 import  DataIngestionPipeline
from PoultryDiseaseClassificationCNN.pipeline.prepare_base_model_pipeline import PrepareBaseModelPipeline

STAGE_NAME = "Data ingestion"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
