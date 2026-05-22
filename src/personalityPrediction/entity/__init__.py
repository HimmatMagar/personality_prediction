from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
      root_dir: Path
      source_url: str
      zip_file: Path
      unzip_file: Path
      

@dataclass
class DataValidationConfig:
      root_dir: Path
      status_file: Path
      file_path: str
      schema: dict


@dataclass
class DataTransformationConfig:
      root_dir: Path
      file_path: Path