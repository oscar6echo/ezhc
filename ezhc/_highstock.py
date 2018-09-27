
from ._wrapper import Wrapper
from ._plot import plot, html, opt_to_dict, opt_to_json
from .scripts import JS_FINANCIAL_TIME_SERIES_0, \
    JS_FINANCIAL_TIME_SERIES_TABLE_1, \
    JS_FINANCIAL_TIME_SERIES_TABLE_2, \
    JS_FINANCIAL_TIME_SERIES_TABLE_OPTIONS_1, \
    JS_FINANCIAL_TIME_SERIES_TABLE_OPTIONS_2, \
    HTML_FINANCIAL_TIME_SERIES_TABLE, \
    JS_FINANCIAL_TIME_SERIES_TABLE_CALLBACK_0, \
    JS_FINANCIAL_TIME_SERIES_TABLE_CALLBACK_1, \
    JS_FINANCIAL_TIME_SERIES_TABLE_CALLBACK_2


class Highstock(Wrapper):
    """
    Main Highstock Object

    API: https://api.highcharts.com/highstock
    Demos: https://www.highcharts.com/stock/demo
    """

    def __init__(self):
        Wrapper.__init__(self, lib='highstock')

        # default config
        self.credits.enabled = False
        self.exporting.enabled = True
        self.chart.animation = False

        self.plotOptions.series.animation = False
        self.plotOptions.line.animation = False
        self.plotOptions.column.animation = False

    def options_as_dict(self, chart_id='chart_id'):
        opt = self.to_dict()
        return opt_to_dict(opt, chart_id=chart_id)

    def options_as_json(self, chart_id='chart_id', save=False, save_name=None, save_path='saved'):
        opt = self.to_dict()
        return opt_to_json(opt, chart_id=chart_id, save=save, save_name=save_name,
                           save_path=save_path)

    def html(self, dated=True, save=False, save_name=None, save_path='saved', notebook=True,
             html_init=None, js_option_postprocess=None, js_extra=None, callback=None,
             version='latest', proxy=None, center=False):
        opt = self.to_dict()
        return html(opt, lib='highstock', dated=dated, save=save, save_name=save_name,
                    save_path=save_path, notebook=notebook,
                    html_init=html_init, js_option_postprocess=js_option_postprocess,
                    js_extra=js_extra, callback=callback, version=version, proxy=proxy,
                    center=center)

    def plot(self, dated=True, save=False, save_name=None, save_path='saved', notebook=True,
             html_init=None, js_option_postprocess=None, js_extra=None, callback=None, footer=None,
             version='latest', proxy=None, center=False):
        """Only Highstock. No add-on."""
        opt = self.to_dict()
        js_extra = JS_FINANCIAL_TIME_SERIES_0
        callback = JS_FINANCIAL_TIME_SERIES_TABLE_CALLBACK_0

        return plot(opt, lib='highstock', dated=dated, save=save, save_name=save_name,
                    save_path=save_path, notebook=notebook,
                    html_init=html_init, js_option_postprocess=js_option_postprocess,
                    js_extra=js_extra, callback=callback, footer=footer, version=version,
                    proxy=proxy, center=center)

    def plot_with_table_1(
            self, dated=True, save=False, save_name=None, save_path='saved', notebook=True,
            footer=None, version='latest', proxy=None):
        """
        Table with Perf, IRR, Vol, Sharpe Ratio, Max Drawdown
        Sharpe ratio is based on time series 'Cash' meaning cash compounded
        If no Cash colmun rates are assumed zero.
        """
        opt = self.to_dict()
        html_init = HTML_FINANCIAL_TIME_SERIES_TABLE
        js_option_postprocess = JS_FINANCIAL_TIME_SERIES_TABLE_OPTIONS_1
        js_extra = JS_FINANCIAL_TIME_SERIES_TABLE_1
        callback = JS_FINANCIAL_TIME_SERIES_TABLE_CALLBACK_1

        return plot(opt, lib='highstock', dated=dated, save=save, save_name=save_name,
                    save_path=save_path, notebook=notebook,
                    html_init=html_init, js_option_postprocess=js_option_postprocess,
                    js_extra=js_extra, callback=callback, footer=footer, 
                    version='latest', proxy=None)

    def plot_with_table_2(
            self, dated=True, save=False, save_name=None, save_path='saved', notebook=True,
            footer=None, version='latest', proxy=None):
        """
        Table with Min, Max, Average, Max Drawdown
        """
        opt = self.to_dict()
        html_init = HTML_FINANCIAL_TIME_SERIES_TABLE
        js_option_postprocess = JS_FINANCIAL_TIME_SERIES_TABLE_OPTIONS_2
        js_extra = JS_FINANCIAL_TIME_SERIES_TABLE_2
        callback = JS_FINANCIAL_TIME_SERIES_TABLE_CALLBACK_2

        return plot(opt, lib='highstock', dated=dated, save=save, save_name=save_name,
                    save_path=save_path, notebook=notebook,
                    html_init=html_init, js_option_postprocess=js_option_postprocess,
                    js_extra=js_extra, callback=callback, footer=footer,
                    version=version, proxy=proxy)
