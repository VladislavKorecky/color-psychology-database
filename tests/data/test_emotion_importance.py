def test_emotion_importance(emotion_data):
    """
    Test if the emotion property "importance" is valid.
    """

    for d in emotion_data:
        importance = d.get("importance")
        importance_length = len(importance)

        assert importance is not None  # check if exists
        assert isinstance(importance, list)  # check data type
        assert importance_length > 0  # check for empty list

        check_importance_types(importance)

        # check if "importance" matches "colors" in length
        colors = d.get("colors")
        colors_length = len(colors)
        assert importance_length == colors_length


def check_importance_types(importance):
    """
    Test individual importance numbers.
    """

    for i in importance:
        assert i is not None  # check if exists
        assert isinstance(i, int) or isinstance(i, float)  # check if its a number
