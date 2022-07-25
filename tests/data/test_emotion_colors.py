# WARNING: do not remove tests.data imports, editors say they are unused but they are necessary!
from tests.data import data
from tests.data import emotion_data


def test_emotion_colors(emotion_data):
    """
    Test if the emotion property "colors" is valid.
    """

    for d in emotion_data:
        colors = d.get("colors")
        colors_length = len(colors)

        assert colors is not None  # check if exists
        assert isinstance(colors, list)  # check data type
        assert colors_length > 0  # check for empty list

        color_check(colors)


def color_check(colors):
    """
    Test individual color values.
    """

    for color in colors:
        assert color is not None  # check if exists
        assert isinstance(color, str)  # check data type
        assert color != ""  # check for content
