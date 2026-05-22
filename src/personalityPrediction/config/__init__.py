from personalityPrediction.entity import *
from personalityPrediction.constants import *
from personalityPrediction.utils import *


class ConfigurationManager:
      
      def __init__(self, config = config, params = params, schema = schema):
            self.config = load_yaml_file(config)
            self.params = load_yaml_file(params)
            self.schema = load_yaml_file(schema)
            
            create_directory([self.config.root_dir])