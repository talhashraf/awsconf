"""Setup module."""
from setuptools import find_packages, setup


def requirements(*names):
    """Combine all requirements from requirement files."""
    return [
        line.strip()
        for name in names
        for line in open(name)
        if line.strip()
    ]


install_requires = requirements("requirements.in")


setup(
    name="awsconf",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
    entry_points={
        "console_scripts": ["awsconf = awsconf.cli:cli"],
    },
    python_requires=">=3.6",
)
