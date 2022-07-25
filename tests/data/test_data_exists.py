# WARNING: do not remove tests.data imports, editors say they are unused but they are necessary!
from tests.data import data


def test_data_exists(data):
    """
    Test if data exists.
    """

    assert data is not None
