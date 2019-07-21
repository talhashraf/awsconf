"""AWS Profiles Builder."""
from awsconf.templates import (
    CONFIG_TEMPLATE,
    CONFIG_WITH_ASSUME_ROLES_TEMPLATE,
    CREDENTIAL_TEMPLATE,
)
from awsconf.utils import load_yaml, merge_dicts


class ConfBuilder:

    def __init__(self, profiles_dir):
        """Initialize everything."""
        # Default configurations for all profiles to inherit.
        config_filename = profiles_dir.joinpath("config.yaml")

        self.config_filename = config_filename
        self.default_config = load_yaml(config_filename)

        self.profiles_dir = profiles_dir

    @property
    def files(self):
        """Return generator for all config files, excluding default config file."""
        for filename in self.profiles_dir.glob("*"):
            if filename == self.config_filename:
                continue

            yield filename

    @property
    def config_profiles(self):
        """Return profiles generator."""
        for filename in self.files:
            data = load_yaml(filename)
            for profile in data["profiles"]:
                profile = merge_dicts(self.default_config, profile)
                yield profile

    @property
    def creds_profiles(self):
        """Return profiles generator."""
        for filename in self.files:
            data = load_yaml(filename)
            for profile in data["profiles"]:
                if profile.get("access_key"):
                    yield profile

    def build(self):
        """Build config file."""
        with open("credentials", "w") as outfile:
            for profile in self.creds_profiles:
                profile_stream = CREDENTIAL_TEMPLATE.render(
                    profile=profile)
                outfile.write(profile_stream)
                outfile.write("\n\n")

        with open("config", "w") as outfile:
            for profile in self.config_profiles:
                for profile_stream in self.parse_config_profile(profile):
                    outfile.write(profile_stream)
                    outfile.write("\n\n")

    def parse_config_profile(self, profile):
        """Parse profile."""
        if "assume_roles" in profile:
            for assume_role in profile["assume_roles"]:
                profile_stream = CONFIG_WITH_ASSUME_ROLES_TEMPLATE.render(
                    profile=profile, assume_role=assume_role)

                yield profile_stream
        else:
            profile_stream = CONFIG_TEMPLATE.render(
                profile=profile)

            yield profile_stream
