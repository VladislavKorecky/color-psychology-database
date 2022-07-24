# WARNING: do not remove tests.data imports, editors say they are unused but they are necessary!
from tests.data import data
from tests.data import emotion_data


def test_emotion_positiveness(emotion_data):
    for d in emotion_data:
        positive = d.get("positive")

        assert positive is not None
        assert isinstance(positive, bool)
