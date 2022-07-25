from json import load

from os import path

from pytest import fixture

from yaml import safe_load


@fixture
def data() -> dict:
    """
    Yield content from data.json file.

    Returns:
        dict: JSON/Dictionary data describing the effects and emotions of colors.
    """

    real_path = path.realpath(__file__)  # get real path of this script
    directory = path.dirname(real_path)  # get directory of the real path

    # open, read and load data
    with open(f"{directory}/../data.json") as f:
        yield load(f)


@fixture
def emotion_data(data) -> list:
    """
    Return data about emotions.

    Args:
        data: Pytest fixture, this is not a normal argument.

    Returns:
        list: List of data about emotions.
    """

    values = []

    # get all values from emotions
    for _, v in data.items():
        values.append(v)

    return values


@fixture
def yaml_data() -> dict:
    """
    Yield content from data.yaml file.

    Returns:
        dict: YAML/Dictionary data describing the effects and emotions of colors.
    """

    real_path = path.realpath(__file__)  # get real path of this script
    directory = path.dirname(real_path)  # get directory of the real path

    # open, read and load data
    with open(f"{directory}/../yaml/data.yaml") as f:
        yield safe_load(f)
