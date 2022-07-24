# WARNING: do not remove tests.data imports, editors say they are unused but they are necessary!
from tests.data import data
from tests.data import emotion_data


def test_emotion_colors(emotion_data):
    for d in emotion_data:
        colors = d.get("colors")

        assert colors is not None
        assert isinstance(colors, list)
        color_check(colors)


def color_check(colors):
    for color in colors:
        assert color is not None
        assert isinstance(color, str)
        assert color != ""
