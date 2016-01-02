
import os
import re
from _config import SCRIPT_DIR


def remove_comments_js(string):
    # remove all streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) 
    # remove all singleline comments (//COMMENT\n ) from string
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) 
    return string   


def load_script(filename, js=True):
    _dir = os.path.dirname(__file__)
    path = os.path.join(_dir, SCRIPT_DIR, filename)
    with open(path) as f:
        contents = f.read()
        if js:
            contents = remove_comments_js(contents)
        return contents#.replace('\n', '')




TOOLTIP_HEADER_FORMAT = '<b>{series.name}</b><br>'
TOOLTIP_POINT_FORMAT_PERCENT = '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>'
TOOLTIP_POINT_FORMAT_OTHER = '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b><br/>'


TOOLTIP_POSITIONER = load_script('tooltip_positioner.js')
FORMATTER_PERCENT = load_script('formatter_percent.js')
FORMATTER_OTHER = load_script('formatter_other.js')

JS_JSON_PARSE = load_script('json_parse.js')

JS_FINANCIAL_TIME_SERIES_TABLE = load_script('financial_time_series_table.js')
HTML_FINANCIAL_TIME_SERIES_TABLE = load_script('financial_time_series_table.html', js=False)
JS_FINANCIAL_TIME_SERIES_TABLE_OPTIONS = load_script('financial_time_series_table_options.js')
JS_FINANCIAL_TIME_SERIES_TABLE_CALLBACK = 'create_table__uuid__'

