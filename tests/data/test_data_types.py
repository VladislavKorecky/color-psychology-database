# WARNING: do not remove tests.data imports, editors say they are unused but they are necessary!
from tests.data import data


def test_data_types(data):
    for key, value in data.items():
        assert isinstance(key, str)
        assert isinstance(value, dict)
