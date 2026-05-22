import os
import yaml
import json
import joblib
from pathlib import Path
from box.config_box import ConfigBox
from personalityPrediction import logging
from ensure import ensure_annotations
from box.exceptions import BoxValueError


@ensure_annotations
def load_yaml_file(yaml_file: Path) -> ConfigBox:
      try:
            with open(yaml_file) as f:
                  content = yaml.safe_load(f)
                  logging.info(f"yaml file: {yaml_file} loaded successfully")
                  return ConfigBox(content)
      except BoxValueError:
            raise ValueError("Yaml file is empty")
      except Exception:
            raise Exception


@ensure_annotations
def create_directory(list_directory: list, verbose=True):
      for filename in list_directory:
            os.makedirs(filename, exist_ok=True)

            if verbose:
                  logging.info(f"File directory: {filename} created successfully")


@ensure_annotations
def save_json(path: Path, data: dict):
      with open(path, 'w') as f:
            json.dump(data, f, indent=4)
      logging.info(f"json file: {path} saved successfully")


@ensure_annotations
def load_file(file:Path):
      with open(file, 'rb') as f:
            data = joblib.load(f)
      return data