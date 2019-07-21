"""Settings module."""
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent

USER_HOME_DIR = Path.home()
DEFAULT_AWS_DIR = USER_HOME_DIR.joinpath(".aws")

TEMPLATES_DIR = PROJECT_DIR.joinpath("templates")
