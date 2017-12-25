
import os
import json
import glob

from IPython.display import Markdown


class Theme:
    """
    Easy access to Highcharts themes
    See https://github.com/highcharts/highcharts/tree/master/js/themes
    """

    def __init__(self):
        here = os.path.dirname(os.path.realpath(__file__))
        paths = glob.glob(os.path.join(here, 'script/themes/*.json'))
        themes = {}
        for path in paths:
            filename = os.path.basename(path).split('.json')[0]
            with open(path, 'r') as f:
                content = f.read()
                dic = json.loads(content)
                themes[filename] = dic
        self.themes = themes

    def info(self):
        li_theme = list(self.themes.keys())
        md = """
Theme contains predtermined [Highcharts themes](https://github.com/highcharts/highcharts/tree/master/js/themes) available as properties
```json
{}
```""".format(li_theme)
        return Markdown(md)
