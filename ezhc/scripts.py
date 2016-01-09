
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
TOOLTIP_POINT_FORMAT_BASIC = '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b><br/>'


TOOLTIP_POSITIONER_CENTER_TOP = load_script('tooltip_positioner_center_top.js')
TOOLTIP_POSITIONER_LEFT_TOP = load_script('tooltip_positioner_left_top.js')
TOOLTIP_POSITIONER_RIGHT_TOP = load_script('tooltip_positioner_right_top.js')

FORMATTER_PERCENT = load_script('formatter_percent.js')
FORMATTER_BASIC = load_script('formatter_basic.js')
FORMATTER_QUANTILE = load_script('formatter_quantile.js')


JS_JSON_PARSE = load_script('json_parse.js')

JS_FINANCIAL_TIME_SERIES_0 = load_script('financial_time_series_0.js')
JS_FINANCIAL_TIME_SERIES_TABLE_1 = load_script('financial_time_series_table_1.js')
JS_FINANCIAL_TIME_SERIES_TABLE_2 = load_script('financial_time_series_table_2.js')
HTML_FINANCIAL_TIME_SERIES_TABLE = load_script('financial_time_series_table.html', js=False)
JS_FINANCIAL_TIME_SERIES_TABLE_OPTIONS = load_script('financial_time_series_table_options.js')
JS_FINANCIAL_TIME_SERIES_TABLE_CALLBACK = 'create_table__uuid__'

