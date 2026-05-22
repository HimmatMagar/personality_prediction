import os
import joblib
from pathlib import Path
from box.config_box import ConfigBox
from personalityPrediction import logging
from personalityPrediction.utils import *
from sklearn.metrics import classification_report
from personalityPrediction.entity import ModelEvalConfig

class ModelEval:
      def __init__(self, config: ModelEvalConfig):
            self.config = config

      
      def eval_mertics(self, actual, pred) -> ConfigBox:
            data = classification_report(actual, pred, output_dict=True)
            return ConfigBox(data)
      
      def val_data(self):
            x_val = load_file(Path(self.config.x_val_file_path))
            y_val = load_file(Path(self.config.y_val_file_path))
            model = joblib.load(self.config.model)

            y_pred = model.predict(x_val)

            data = self.eval_mertics(y_val, y_pred)

            Model_Report = {
                  'Class_0': {
                        'precision': data['0']['precision'],
                        'recall': data['0']['recall'],
                        'f1-score': data['0']['f1-score'],
                        'support': data['0']['support']
                  },
                  'Class_1': {
                        'precision': data['1']['precision'],
                        'recall': data['1']['recall'],
                        'f1-score': data['1']['f1-score'],
                        'support': data['1']['support']
                  },
                  'accuracy': data['accuracy'],
            }
            save_json(path=Path(self.config.metric), data = Model_Report)
            logging.info(f"Model evaluation successfully and report saved on: {self.config.metric}")