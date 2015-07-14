
from _wrapper import Wrapper
from _plot import plot, html



class Highcharts(Wrapper):
    """
    Main Highcharts Object

    API: http://api.highcharts.com/highcharts
    Demos: http://www.highcharts.com/demo
    """

    def __init__(self):
        Wrapper.__init__(self, lib='highcharts')

        #default config
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


    def plot(self, save=False, js_preprocess=None, callback=None):
        opt = self.to_dict()
        return plot(opt, lib='highcharts', save=save, js_preprocess=js_preprocess, callback=callback)

    def html(self, save=False, js_preprocess=None, callback=None):
        opt = self.to_dict()
        return html(opt, lib='highcharts', save=save, js_preprocess=js_preprocess, callback=callback)
