"""Python module for example configuration and paths."""

from pathlib import Path

PROJECT_NAME: str = "example"
"""Name of the project."""
ROOT_FOLDER_NAME: str = f".{PROJECT_NAME}"
"""Name of the root folder."""
ROOT_FOLDER_PATH: Path = Path.home() / ROOT_FOLDER_NAME
"""Path to the root folder."""
LOG_FILE_PATH: Path = ROOT_FOLDER_PATH / "main.log"
"""Path to the log file."""
CONFIG_FILE_PATH: Path = ROOT_FOLDER_PATH / "config.json"
"""Path to the config file."""
