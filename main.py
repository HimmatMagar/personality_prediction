from personalityPrediction import logging
from personalityPrediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline
# from churn_prediction.pipeline.data_transform_pipeline import DataTransformPipeline
# from churn_prediction.pipeline.model_pipeline import ModelBuildingPipeline
# from churn_prediction.pipeline.model_eval_pipeline import ModelEvalPipeline

STAGE_NAME = "Data Ingestion stage"
try:
      logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = DataIngestionPipeline()
      obj.main()
      logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e