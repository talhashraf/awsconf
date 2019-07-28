"""AWS Profiles Builder."""
import logging

from awsconf.settings import AWS_CONF_FILE, AWS_CRED_FILE
from awsconf.templates import CONFIG_TEMPLATE, CREDENTIAL_TEMPLATE
from awsconf.utils import load_yaml


logger = logging.getLogger(__name__)


class Builder:
    """Configuration Builder."""

    def __init__(self, filename):
        """Initialize everything."""
        logger.info("Reading profiles: %s", filename)
        self.config = load_yaml(filename)

    def build_config(self):
        """Build config."""
        logger.info("Generating config: %s", AWS_CONF_FILE)
        stream = CONFIG_TEMPLATE.render(config=self.config)
        with open(AWS_CONF_FILE, "w") as outfile:
            outfile.write(stream)

    def build_credentials(self):
        """Build credentials."""
        logger.info("Generating credentials: %s", AWS_CRED_FILE)
        stream = CREDENTIAL_TEMPLATE.render(config=self.config)
        with open(AWS_CRED_FILE, "w") as outfile:
            outfile.write(stream)
