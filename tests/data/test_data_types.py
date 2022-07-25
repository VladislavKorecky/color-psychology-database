# WARNING: do not remove tests.data imports, editors say they are unused but they are necessary!
from tests.data import data


def test_data_types(data):
    """
    Test if keys and values of emotion items have the correct type.
    """

    for key, value in data.items():
        assert isinstance(key, str)  # check for key type
        assert isinstance(value, dict)  # check for value type
