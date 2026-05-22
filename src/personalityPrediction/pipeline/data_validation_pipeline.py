from personalityPrediction import logging
from personalityPrediction.config import ConfigurationManager
from personalityPrediction.components.data_validation import DataValidation

STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline():
      def __init__(self):
            pass

      def main(self):
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(data_validation_config)
            data_validation.validate_column()
      
if __name__ == "__main__":
      try:
            logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = DataValidationPipeline()
            obj.main()
            logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logging.exception(e)
            raise e