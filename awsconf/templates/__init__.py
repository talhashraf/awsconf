"""Templates configurations."""
from jinja2 import Template

from awsconf.settings import TEMPLATES_DIR


with open(TEMPLATES_DIR.joinpath("credential")) as stream:
    CREDENTIAL_TEMPLATE = Template(stream.read())

with open(TEMPLATES_DIR.joinpath("config")) as stream:
    CONFIG_TEMPLATE = Template(stream.read())

with open(TEMPLATES_DIR.joinpath("config-with-assume-roles")) as stream:
    CONFIG_WITH_ASSUME_ROLES_TEMPLATE = Template(stream.read())
