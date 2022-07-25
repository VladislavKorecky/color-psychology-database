def test_emotion_text(emotion_data):
    """
    Test if the emotion property "text" is valid.
    """

    for d in emotion_data:
        text = d.get("text")

        assert text is not None  # check if exists
        assert isinstance(text, str)  # check data type
        assert text != ""  # check for content
