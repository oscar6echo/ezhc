
import sys
import os
import json
from ._config import HC_OPTION_FILE, HC_OBJECT_FILE, \
                    HS_OPTION_FILE, HS_OBJECT_FILE, \
                    API_DIR


def load_resource(src):
    _dir = os.path.dirname(__file__)
    object_builder_file = os.path.join(_dir, API_DIR, src)
    if sys.version_info.major == 3:
        with open(object_builder_file, encoding='UTF-8') as obj_build:
            return json.load(obj_build)
    else:
        with open(object_builder_file) as obj_build:
            return json.load(obj_build)


class State(object):
    """
    Contains all 'highcharts' or 'highstock' API
    Select lib='highcharts' or lib='highstock'
    """

    def __init__(self, lib='highcharts'):
        if lib == 'highcharts':
            self._OBJECT = load_resource(HC_OBJECT_FILE)
            self._OPTION = load_resource(HC_OPTION_FILE)
        elif lib == 'highstock':
            self._OBJECT = load_resource(HS_OBJECT_FILE)
            self._OPTION = load_resource(HS_OPTION_FILE)
        else:
            raise ValueError("Wrong lib, 'highcharts' or 'highstock' expected")

state_HC = State(lib='highcharts')
state_HS = State(lib='highstock')
