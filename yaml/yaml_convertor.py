"""
This script converts JSON data inside of data.json (one directory back) into YAML and dumps it into data.yaml file.
The user can also optionally pass an argument with the path to the data.json file in case it is elsewhere.
"""

from os import path

from json import load
from sys import argv

from yaml import dump


def get_json_data_path() -> str:
    """
    Return an absolute path to the data.json file.

    Returns:
        str: Path to the JSON file.
    """

    # check if argument was passed, True if it wasn't
    if len(argv) == 1:
        real_path = path.realpath(__file__)  # get real path of this script
        return path.dirname(real_path) + "/../data.json"  # get directory of the real path

    return argv[1]


def get_json_data() -> dict:
    """
    Return content from data.json file.

    Returns:
        dict: JSON/Dictionary data describing the effects and emotions of colors.
    """

    json_path = get_json_data_path()

    # open, read and load data
    with open(json_path) as json_f:
        return load(json_f)


if __name__ == '__main__':
    # get json data
    json_data = get_json_data()

    # write data to yaml
    with open(f"data.yaml", "w") as yaml_f:
        dump(json_data, yaml_f)
