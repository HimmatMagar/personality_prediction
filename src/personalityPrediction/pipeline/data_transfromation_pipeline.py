import joblib
from personalityPrediction import logging
from personalityPrediction.config import ConfigurationManager
from personalityPrediction.components.data_transformation import DataTransformation

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline():
      def __init__(self):
            pass


      def main(self):
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transform = DataTransformation(data_transformation_config)
            data_transform.transform_data()
      
if __name__ == "__main__":
      try:
            logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = DataTransformationPipeline()
            obj.main()
            logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logging.exception(e)
            raise e
      