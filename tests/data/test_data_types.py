def test_data_types(data):
    """
    Test if keys and values of emotion items have the correct type.
    """

    for key, value in data.items():
        assert isinstance(key, str)  # check for key type
        assert isinstance(value, dict)  # check for value type
