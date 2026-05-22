from personalityPrediction import logging
from personalityPrediction.config import ConfigurationManager
from personalityPrediction.components.model_eval import ModelEval

STAGE_NAME = "Model Eval Stage"

class ModelEvalPipeline():
      def __init__(self):
            pass

      def main(self):
            config = ConfigurationManager()
            model_eval_config = config.get_model_eval_config()
            model = ModelEval(model_eval_config)
            model.val_data()
      
if __name__ == "__main__":
      try:
            logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = ModelEvalPipeline()
            obj.main()
            logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logging.exception(e)
            raise e