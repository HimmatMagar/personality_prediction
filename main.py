from personalityPrediction import logging
from personalityPrediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from personalityPrediction.pipeline.data_transfromation_pipeline import DataTransformationPipeline
from personalityPrediction.pipeline.model_building_pipeline import ModelBuildPipeline
# from churn_prediction.pipeline.model_eval_pipeline import ModelEvalPipeline
from personalityPrediction.pipeline.data_validation_pipeline import DataValidationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
      logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = DataIngestionPipeline()
      obj.main()
      logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logging.exception(e)
      raise e


STAGE_NAME = "Data Validation Stage"
try:
      logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = DataValidationPipeline()
      obj.main()
      logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logging.exception(e)
      raise e


STAGE_NAME = "Data Transformation Stage"
try:
      logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = DataTransformationPipeline()
      obj.main()
      logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logging.exception(e)
      raise e


STAGE_NAME = "Model building Stage"
try:
      logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = ModelBuildPipeline()
      obj.main()
      logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logging.exception(e)
      raise e
