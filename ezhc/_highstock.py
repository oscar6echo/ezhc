
from _wrapper import Wrapper
from _plot import plot, html



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


    def plot(self, save=False, js_preprocess=None, callback=None):
        opt = self.to_dict()
        return plot(opt, lib='highstock', save=save, js_preprocess=js_preprocess, callback=callback)


    def html(self, save=False, js_preprocess=None, callback=None):
        opt = self.to_dict()
        return html(opt, lib='highstock', save=save, js_preprocess=js_preprocess, callback=callback)

