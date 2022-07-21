# Color Psychology Database
Color Psychology Database is a collection of data, describing the emotions and psychological effects of colors.

## Repository description
- data.json - JSON file containing the color psychology data. Visit [Data content](#data-content) for more information.
- yaml
  1. yaml_converter.py - python script able to convert JSON files to YAML
  2. data.yaml - YAML version of data.json, data.yaml is regularly updated, but might not be always up-to-date. If you want to make sure, run the yaml_converter.py or use the JSON version instead.

### Data contnet
`
{
    "some_emotion_or_effect": {
        "positive": true,
        "text": "some emotion or effect",
        "colors": [
            "color1",
            "color2"
        ],
        "importance": [
            1,
            5.76
        ]
    },
    "another_emotion_or_effect": {
        "positive": false,
        "text": "emotion",
        "colors": [
            "red",
            "green",
            "blue"
        ],
        "importance": [
            -6,
            0,
            10000000
        ]
    }
}
`
- "another_emotion_or_effect" and "some_emotion_or_effect" are keys/ids of the emotions and are used to group and label their corresponding data so that it can be easily found and used.
- "positive" defines if the emotion is positive/wanted, in which case its value is "true or if the emotion is negative/a side effect, which is indicated by the value "false"
- "text" is the name of the effect/emotion. It is usually the same as the key but without underscores, but it is not a rule.
- "colors" is a list of colors that relate to the effect/emotion.
- "importance" defines how strongly are emotions and color related. The color and importance are in the same position (element-wise operation), which means that the first color responds to the first number, the second color to the second number, and so on. The numbers range from infinity to -infinity (infinities not included), including integers and floating points. A higher number means that the color is more tightly related to the emotion/effect.


## License
This project is under the MIT License. For more info, read the "LICENSE" file or check out [TLDRLegal](https://tldrlegal.com/license/mit-license) for a quick summary.

## Data origin:
- **[Empowered by color](https://www.empower-yourself-with-color-psychology.com/)** - main source 
- Project contributors
- Other/Unknown
