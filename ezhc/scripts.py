
import os
import re
from jinja2 import Environment

from ._config import SCRIPT_DIR
from ._img import image_src


def get_path(filename):
    _dir = os.path.dirname(__file__)
    path = os.path.join(_dir, SCRIPT_DIR, filename)
    return path


def remove_comments_js(string):
    # remove all streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", string)
    # remove all singleline comments (//COMMENT\n ) from string
    string = re.sub(re.compile("//.*?\n"), "", string)
    return string


def load_script(filename, js=True):
    path = get_path(filename)
    with open(path) as f:
        contents = f.read()
        if js:
            contents = remove_comments_js(contents)
        return contents  # .replace('\n', '')


def from_template(contents, **kwargs):
    contents = Environment().from_string(contents).render(**kwargs)
    return contents


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
JS_FINANCIAL_TIME_SERIES_TABLE_OPTIONS_1 = load_script('financial_time_series_table_options_1.js')
JS_FINANCIAL_TIME_SERIES_TABLE_OPTIONS_2 = load_script('financial_time_series_table_options_2.js')
JS_FINANCIAL_TIME_SERIES_TABLE_CALLBACK_0 = 'function(chart) { create_table_0("__uuid__", chart); }'
JS_FINANCIAL_TIME_SERIES_TABLE_CALLBACK_1 = 'function(chart) { console.log("callback_1 beg "+"__uuid__"); create_table_1("__uuid__", chart); }'
JS_FINANCIAL_TIME_SERIES_TABLE_CALLBACK_2 = 'function(chart) { create_table_2("__uuid__", chart); }'

TEMPLATE_DISCLAIMER = load_script('template_disclaimer.html', js=False)

PATH_TO_LOGO_JUPYTER = image_src(get_path('Jupyter_logo.png'))
PATH_TO_LOGO_SG = image_src(get_path('SG_logo.png'))
