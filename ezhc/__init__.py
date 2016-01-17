

from _config import load_js_libs


from ._highcharts import Highcharts
from ._highstock import Highstock
import sample
import build
from ._clock import Clock


__all__ = ['Highcharts',
           'Highstock',
           'samples',
           'build',
           'Clock',
           ]


load_js_libs()
print 'Open console to check js libs were loaded in page'

__author__ = 'oscar6eho'
