from json import load

from os import path


def test_yaml(yaml_data):
    """
    Test if data from data.json is the same as data from data.yaml.
    """

    json_data = get_json_data()
    assert json_data == yaml_data


def get_json_data():
    """
    Return content from data.json file.

    Returns:
        dict: JSON/Dictionary data describing the effects and emotions of colors.
    """

    real_path = path.realpath(__file__)  # get real path of this script
    directory = path.dirname(real_path)  # get directory of the real path

    # open, read and load data
    with open(f"{directory}/../../data.json") as f:
        return load(f)
