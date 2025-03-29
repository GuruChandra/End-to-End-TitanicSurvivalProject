from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: Path
    local_data_file: Path
    unzip_dir: Path

from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataValidatioConfig:
   root_dir: Path
   status_file: Path
   ALL_REQUIRED_FILES: list


@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path