"""Command-Line Interface."""
import logging

import click

from awsconf.builder import ConfBuilder
from awsconf.settings import DEFAULT_AWS_DIR, PROJECT_DIR


@click.group()
def cli():
    """Command-Line Interface for awsconf."""
    log_format = "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_format)


@cli.command("build")
@click.option(
    "--profiles-dir",
    type=click.Path(exists=True),
    default=PROJECT_DIR.parent.joinpath("profiles"),
    # default=DEFAULT_AWS_DIR.joinpath("profiles"),
    help="Directory from where the system will read YAML config/profiles.",
)
def build(profiles_dir):
    """Build AWS configurations and credentials files."""
    logging.info("Profiles Directory: %s", profiles_dir)

    builder = ConfBuilder(profiles_dir)
    builder.build()


@cli.command("final-build")
@click.option(
    "--profiles-dir",
    type=click.Path(exists=True),
    default=DEFAULT_AWS_DIR.joinpath("profiles"),
    help="Directory from where the system will read YAML config/profiles.",
)
def final_build(profiles_dir):
    """Build AWS configurations and credentials files."""
    logging.info("Profiles Directory: %s", profiles_dir)

    builder = ConfBuilder(profiles_dir)
    builder.build()


if __name__ == "__main__":
    cli()
