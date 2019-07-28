"""Templates configurations."""
from jinja2 import Environment, FileSystemLoader

from awsconf.settings import PROJECT_DIR


TEMPLATES_DIR = PROJECT_DIR.joinpath("templates")

# Initiate template loader.
template_loader = FileSystemLoader(searchpath=str(TEMPLATES_DIR))
template_env = Environment(
    loader=template_loader,
    trim_blocks=True,
    lstrip_blocks=True,
    keep_trailing_newline=True,
)

CREDENTIAL_TEMPLATE = template_env.get_template("credential")
CONFIG_TEMPLATE = template_env.get_template("config")
