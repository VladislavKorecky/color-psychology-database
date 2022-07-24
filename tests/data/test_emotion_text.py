# WARNING: do not remove tests.data imports, editors say they are unused but they are necessary!
from tests.data import data
from tests.data import emotion_data


def test_emotion_text(emotion_data):
    for d in emotion_data:
        text = d.get("text")

        assert text is not None
        assert isinstance(text, str)
        assert text != ""
