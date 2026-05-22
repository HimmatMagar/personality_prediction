from personalityPrediction import logging
from personalityPrediction.components.data_ingestion import DataIngestion
from personalityPrediction.config import ConfigurationManager


STAGE_NAME = "Data Ingestion stage"

class DataIngestionPipeline():
      def __init__(self):
            pass

      def main(self):
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingetion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.unzip_file()
            
if __name__ == "__main__":
      try:
            logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = DataIngestionPipeline()
            obj.main()
            logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logging.exception(e)
            raise e