import os
import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from personalityPrediction import logging
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from personalityPrediction.entity import DataTransformationConfig
from sklearn.preprocessing import StandardScaler, LabelEncoder, OrdinalEncoder


class DataTransformation:
      def __init__(self, config: DataTransformationConfig):
            self.config = config


      def transform_data(self):
            df = pd.read_csv(self.config.file_path)
            df.columns = df.columns.str.lower().str.strip()
            
            df.drop_duplicates(inplace=True)
            
            X = df.drop(columns='personality')
            y = df['personality']

            x_train, x_val, y_train, y_val = train_test_split(
                  X,
                  y,
                  test_size=0.3
            )

            encoder = LabelEncoder()
            yTrain = encoder.fit_transform(y_train)
            yTest = encoder.transform(y_val)

            # Assuming x has columns: age (0), gender (1), visa_type (2), documents_submitted (3)
            pipeline = Pipeline([
                  ("Preprocess", ColumnTransformer(
                        transformers = [
                              ("cate_columns", Pipeline([
                                    ('cate_impute', SimpleImputer(strategy="most_frequent")),
                                    ('encoder', OrdinalEncoder())
                              ]), [1, 4]),
                              ("numeric_col", Pipeline([
                                    ("numeric_imputer", SimpleImputer(strategy="mean")),
                                    ("scale", StandardScaler())
                              ]), [0, 2, 3, 5, 6])
                        ],
                        remainder='passthrough'
                  ))
            ])
            
            x_train_transformed = pipeline.fit_transform(x_train)
            x_val_transformed = pipeline.transform(x_val)
            joblib.dump(pipeline, os.path.join(self.config.root_dir, 'preprocessor.pkl'))

            joblib.dump(x_train_transformed, os.path.join(self.config.root_dir, "x_train.pkl"))
            joblib.dump(x_val_transformed, os.path.join(self.config.root_dir, "x_val.pkl"))
            joblib.dump(yTrain, os.path.join(self.config.root_dir, "y_train.pkl"))
            joblib.dump(yTest, os.path.join(self.config.root_dir, "y_val.pkl"))

            logging.info("Split data successfully")