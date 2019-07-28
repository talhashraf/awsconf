"""Command-Line Interface."""
import logging

import click

from awsconf.builder import Builder
from awsconf.settings import DEFAULT_AWS_DIR


@click.group()
def cli():
    """Command-Line Interface for awsconf."""
    log_format = "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_format)


@cli.command("build")
@click.option(
    "--profiles-file",
    type=click.Path(exists=True),
    default=DEFAULT_AWS_DIR.joinpath("profiles.yaml"),
    help="File path from where the system will read YAML profiles.",
)
@click.option(
    "--no-credentials",
    type=bool,
    default=False,
    help="True means it will not generate credentials file.",
)
@click.option(
    "--no-config",
    type=bool,
    default=False,
    help="True means it will not generate config file.",
)
def build(profiles_file, no_credentials, no_config):
    """Build AWS configurations and credentials files."""
    builder = Builder(profiles_file)

    if not no_credentials:
        builder.build_config()

    if not no_config:
        builder.build_credentials()


if __name__ == "__main__":
    cli()
