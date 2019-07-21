"""Settings module."""
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent

USER_HOME_DIR = Path.home()
DEFAULT_AWS_DIR = USER_HOME_DIR.joinpath(".aws")
AWS_CONF_FILE = DEFAULT_AWS_DIR.joinpath("config")
AWS_CRED_FILE = DEFAULT_AWS_DIR.joinpath("credentials")

TEMPLATES_DIR = PROJECT_DIR.joinpath("templates")
