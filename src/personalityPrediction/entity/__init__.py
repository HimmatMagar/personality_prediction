from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
      root_dir: Path
      source_url: str
      zip_file: Path
      unzip_file: Path
      

@dataclass(frozen=True)
class DataValidationConfig:
      root_dir: Path
      status_file: Path
      file_path: str
      schema: dict


@dataclass(frozen=True)
class DataTransformationConfig:
      root_dir: Path
      file_path: Path

@dataclass(frozen=True)
class ModelBuildingConfig:
      root_dir: Path
      x_train_file_path: Path
      y_train_file_path: Path
      colsample_bytree: float
      learning_rate: float
      max_depth: int
      n_estimators: int
      subsample: float
      model: str


@dataclass(frozen=True)
class ModelEvalConfig:
      root_dir: Path
      x_val_file_path: Path
      y_val_file_path: Path
      model: Path
      metric: Path