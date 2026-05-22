from personalityPrediction import logging
from personalityPrediction.config import ConfigurationManager
from personalityPrediction.components.model_building import ModelBuilding

STAGE_NAME = "Model building Stage"

class ModelBuildPipeline():
      def __init__(self):
            pass

      def main(self):
            config = ConfigurationManager()
            model_train_config = config.get_model_train_config()
            model = ModelBuilding(model_train_config)
            model.build_model()
      
if __name__ == "__main__":
      try:
            logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = ModelBuildPipeline()
            obj.main()
            logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logging.exception(e)
            raise e