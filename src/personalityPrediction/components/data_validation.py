import pandas as pd
from personalityPrediction import logging
from personalityPrediction.entity import DataValidationConfig


class DataValidation:
      def __init__(self, config: DataValidationConfig):
            self.config = config

      
      def validate_column(self) -> bool:
           try:
                  data = pd.read_csv(self.config.file_path)
            
                  all_column = list(data.columns)
                  schema = self.config.schema.keys()


                  for col in all_column:
                        if col not in schema:
                              validation_status = False
                              with open(self.config.status_file, 'w') as f:
                                    f.write(f"Validation Status: {validation_status}")
                        else:
                              validation_status = True
                              with open(self.config.status_file, 'w') as f:
                                    f.write(f"Validation Status: {validation_status}")
                  
                  logging.info("Validation status written successfully")
            
           except Exception:
                 raise Exception