
from ._wrapper import Wrapper
from ._plot import plot, html, opt_to_dict, opt_to_json


class Highcharts(Wrapper):
    """
    Main Highcharts Object

    API: https://api.highcharts.com/highcharts
    Demos: https://www.highcharts.com/demo
    """

    def __init__(self):
        Wrapper.__init__(self, lib='highcharts')

        # default config
        self.credits.enabled = False
        self.exporting.enabled = True
        self.chart.animation = False
        self.series.animation = False

        self.plotOptions.series.animation = False
        self.plotOptions.line.animation = False
        self.plotOptions.column.animation = False
        self.plotOptions.bar.animation = False
        self.plotOptions.pie.animation = False
        self.plotOptions.scatter.animation = False
        self.plotOptions.bubble.animation = False
        self.plotOptions.treemap.animation = False

    def options_as_dict(self, chart_id='chart_id'):
        opt = self.to_dict()
        return opt_to_dict(opt, chart_id=chart_id)

    def options_as_json(self, chart_id='chart_id', save=False, save_name=None, save_path='saved'):
        opt = self.to_dict()
        return opt_to_json(opt, chart_id=chart_id, save=save, save_name=save_name,
                           save_path=save_path)

    def plot(self, dated=True, save=False, save_name=None, save_path='saved', notebook=True,
             html_init=None, js_option_postprocess=None, js_extra=None, callback=None,
             version='latest', proxy=None, center=False):
        opt = self.to_dict()
        return plot(opt, lib='highcharts', dated=dated, save=save, save_name=save_name,
                    save_path=save_path, notebook=notebook,
                    html_init=html_init, js_option_postprocess=js_option_postprocess,
                    js_extra=js_extra, callback=callback, version=version, proxy=proxy,
                    center=center)

    def html(self, dated=True, save=False, save_name=None, save_path='saved', notebook=True,
             html_init=None, js_option_postprocess=None, js_extra=None, callback=None,
             version='latest', proxy=None, center=False):
        opt = self.to_dict()
        return html(opt, lib='highcharts', dated=dated, save=save, save_name=save_name,
                    save_path=save_path, notebook=notebook,
                    html_init=html_init, js_option_postprocess=js_option_postprocess,
                    js_extra=js_extra, callback=callback, version=version, proxy=proxy,
                    center=center)
