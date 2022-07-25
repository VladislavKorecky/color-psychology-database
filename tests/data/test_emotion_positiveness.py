def test_emotion_positiveness(emotion_data):
    """
    Test if the emotion property "positive" is valid.
    """

    for d in emotion_data:
        positive = d.get("positive")

        assert positive is not None  # check if exists
        assert isinstance(positive, bool)  # check data type
