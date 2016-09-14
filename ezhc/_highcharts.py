
from ._wrapper import Wrapper
from ._plot import plot, html


class Highcharts(Wrapper):
    """
    Main Highcharts Object

    API: http://api.highcharts.com/highcharts
    Demos: http://www.highcharts.com/demo
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

    def plot(self, dated=True, save=False, save_name=None, html_init=None,
             js_option_postprocess=None, js_extra=None, callback=None):
        opt = self.to_dict()
        return plot(opt, lib='highcharts', dated=dated, save=save, save_name=save_name,
                    html_init=html_init, js_option_postprocess=js_option_postprocess,
                    js_extra=js_extra, callback=callback)

    def html(self, dated=True, save=False, save_name=None, html_init=None,
             js_option_postprocess=None, js_extra=None, callback=None):
        opt = self.to_dict()
        return html(opt, lib='highcharts', dated=dated, save=save, save_name=save_name,
                    html_init=html_init, js_option_postprocess=js_option_postprocess,
                    js_extra=js_extra, callback=callback)
