import os
import joblib
from pathlib import Path
from xgboost import XGBClassifier
from personalityPrediction import logging
from personalityPrediction.utils import *
from personalityPrediction.entity import ModelBuildingConfig


class ModelBuilding:
      def __init__(self, config: ModelBuildingConfig):
            self.config = config

      def build_model(self) -> None:
            x_train = load_file(Path(self.config.x_train_file_path))
            y_train = load_file(Path(self.config.y_train_file_path))

            model = XGBClassifier(
                  colsample_bytree = self.config.colsample_bytree,
                  learning_rate = self.config.learning_rate,
                  max_depth = self.config.max_depth,
                  n_estimators = self.config.n_estimators,
                  subsample = self.config.subsample
            )

            model.fit(x_train, y_train)

            model_path = os.path.join(self.config.root_dir, self.config.model)
            with open(model_path, "wb") as f:
                  joblib.dump(model, f)
            logging.info(f"Model building successfully in: {model}")