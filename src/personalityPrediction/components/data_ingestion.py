import os
import zipfile
import urllib.request as req
from personalityPrediction import logging
from personalityPrediction.entity import DataIngestionConfig



class DataIngestion:

      def __init__(self, config: DataIngestionConfig):
            self.config = config
      

      def download_file(self):
            if not os.path.exists(self.config.zip_file):
                  filename, header = req.urlretrieve(
                        url=self.config.source_url,
                        filename=self.config.zip_file
                  )
                  logging.info(f"{filename} downloaded with following info: \n{header}")
            else:
                  logging.info("file is already exist")

      
      def unzip_file(self):
            unzip_file = self.config.unzip_file
            os.makedirs(unzip_file, exist_ok=True)
            with zipfile.ZipFile(self.config.zip_file, 'r') as f:
                  f.extractall(unzip_file)