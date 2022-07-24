# WARNING: do not remove tests.data imports, editors say they are unused but they are necessary!
from tests.data import data


def test_data_exists(data):
    assert data is not None
