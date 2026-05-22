from personalityPrediction.entity import *
from personalityPrediction.constants import *
from personalityPrediction.utils import *


class ConfigurationManager:
      
      def __init__(self, config = config, params = params, schema = schema):
            self.config = load_yaml_file(config)
            self.params = load_yaml_file(params)
            self.schema = load_yaml_file(schema)
            
            create_directory([self.config.root_dir])
            
      
      def get_data_ingetion_config(self) -> DataIngestionConfig:
            config = self.config.data_ingestion
            create_directory([config.root_dir])
            
            return DataIngestionConfig (
                  root_dir = config.root_dir,
                  source_url = config.source_url,
                  zip_file = config.zip_file,
                  unzip_file = config.unzip_file
            )
            
      def get_data_validation_config(self) -> DataValidationConfig:
            config = self.config.data_validation
            schema = self.schema.column

            create_directory([config.root_dir])

            return DataValidationConfig(
                  root_dir=config.root_dir,
                  status_file=config.status_file,
                  file_path=config.file_path,
                  schema = schema
            )
            
      def get_data_transformation_config(self) -> DataTransformationConfig:
            config = self.config.data_transformation

            create_directory([config.root_dir])

            data_transformation_config = DataTransformationConfig(
                  root_dir=config.root_dir,
                  file_path=config.file_path
            )

            return data_transformation_config