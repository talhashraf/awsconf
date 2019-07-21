"""Project Utilities."""
import yaml


def load_yaml(filename):
    """Return JSON data for given YAML file."""
    with open(filename, "r") as stream:
        return yaml.safe_load(stream)


def merge_dicts(base_item, new_item):
    """Put base item values in new item (if unique keys are found)."""
    for key in base_item:
        if key not in new_item:
            new_item[key] = base_item[key]

    return new_item
