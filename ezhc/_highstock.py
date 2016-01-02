
from _wrapper import Wrapper
from _plot import plot, html
from scripts import JS_FINANCIAL_TIME_SERIES_TABLE, \
                    JS_FINANCIAL_TIME_SERIES_TABLE_OPTIONS, \
                    HTML_FINANCIAL_TIME_SERIES_TABLE, \
                    JS_FINANCIAL_TIME_SERIES_TABLE_CALLBACK


class Highstock(Wrapper):
    """
    Main Highstock Object

    API: http://api.highcharts.com/highstock
    Demos: http://www.highcharts.com/stock/demo
    """

    def __init__(self):
        Wrapper.__init__(self, lib='highstock')

        #default config
        self.credits.enabled = False
        self.exporting.enabled = True
        self.chart.animation = False
        
        self.plotOptions.series.animation = False
        self.plotOptions.line.animation = False
        self.plotOptions.column.animation = False


    def plot(self, save=False, save_name=None, html_init=None,
             js_option_postprocess=None, js_extra=None, callback=None):
        opt = self.to_dict()
        return plot(opt, lib='highstock', save=save, save_name=save_name,
            html_init=html_init, js_option_postprocess=js_option_postprocess,
            js_extra=js_extra, callback=callback)


    def html(self, save=False, save_name=None, html_init=None,
             js_option_postprocess=None, js_extra=None, callback=None):
        opt = self.to_dict()
        return html(opt, lib='highstock', save=save, save_name=save_name,
            html_init=html_init, js_option_postprocess=js_option_postprocess,
            js_extra=js_extra, callback=callback)

    def plot_with_table(self, save=False, save_name=None):
        """
        Sharpe ratio is based on time series 'Cash' meaning cash compounded
        If no Cash colmun rates are assumed zero.
        """
        opt = self.to_dict()
        html_init = HTML_FINANCIAL_TIME_SERIES_TABLE
        js_option_postprocess = JS_FINANCIAL_TIME_SERIES_TABLE_OPTIONS
        js_extra = JS_FINANCIAL_TIME_SERIES_TABLE
        callback = JS_FINANCIAL_TIME_SERIES_TABLE_CALLBACK

        return plot(opt, lib='highstock', save=save, save_name=save_name,
            html_init=html_init, js_option_postprocess=js_option_postprocess,
            js_extra=js_extra, callback=callback)

