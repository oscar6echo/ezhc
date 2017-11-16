
from ._highcharts import Highcharts



class Clock(Highcharts):
    """
    Highcharts Clock
    https://jsfiddle.net/gh/get/jquery/1.9.1/highslide-software/highcharts.com/tree/master/samples/highcharts/demo/gauge-clock/
    """

    def __init__(self):

        Highcharts.__init__(self)

        self.js_extra = """
        function getNow() {
            var now = new Date();

            return {
                hours: now.getHours() + now.getMinutes() / 60,
                minutes: now.getMinutes() * 12 / 60 + now.getSeconds() * 12 / 3600,
                seconds: now.getSeconds() * 12 / 60
            };
        }

        var now = getNow();

        function pad(number, length) {
            // Create an array of the remaining length + 1 and join it with 0's
            return new Array((length || 2) + 1 - String(number).length).join(0) + number;
        }


        // Extend jQuery with some easing (copied from jQuery UI)
        $.extend($.easing, {
            easeOutElastic: function (x, t, b, c, d) {
                var s=1.70158;var p=0;var a=c;
                if (t==0) return b;  if ((t/=d)==1) return b+c;  if (!p) p=d*.3;
                if (a < Math.abs(c)) { a=c; var s=p/4; }
                else var s = p/(2*Math.PI) * Math.asin (c/a);
                return a*Math.pow(2,-10*t) * Math.sin( (t*d-s)*(2*Math.PI)/p ) + c + b;
            }
        });
        """

        self.callback = """
        function (chart) {
            setInterval(function () {

                now = getNow();

                var hour = chart.get('hour'),
                    minute = chart.get('minute'),
                    second = chart.get('second'),
                    // run animation unless we're wrapping around from 59 to 0
                    animation = now.seconds === 0 ? false : { easing: 'easeOutElastic' };

                // Cache the tooltip text
                chart.tooltipText =
                    pad(Math.floor(now.hours), 2) + ':' +
                    pad(Math.floor(now.minutes * 5), 2) + ':' +
                    pad(now.seconds * 5, 2);

                hour.update(now.hours, true, animation);
                minute.update(now.minutes, true, animation);
                second.update(now.seconds, true, animation);

            }, 1000);
        }
        """

        self.g = Highcharts()

        self.g.chart = {
            'type': 'gauge',
            'plotBackgroundColor': None,
            'plotBackgroundImage': None,
            'plotBorderWidth': 0,
            'plotShadow': False,
            'height': 250
        }

        self.g.title.text = 'The Highcharts Clock'

        self.g.pane.background = [
            # default background
            {},
            # reflex for supported browsers
            {'backgroundColor': {
                'radialGradient': {
                    'cx': 0.5,
                    'cy': -0.4,
                    'r': 1.9
                },
                'stops': [
                    [0.5, 'rgba(255, 255, 255, 0.2)'],
                    [0.5, 'rgba(200, 200, 200, 0.2)']
                ]
            }}
        ]

        self.g.yAxis = {
            'labels': { 'distance': -20 },
            'min': 0,
            'max': 12,
            'lineWidth': 0,
            'showFirstLabel': False,

            'minorTickInterval': 'auto',
            'minorTickWidth': 1,
            'minorTickLength': 5,
            'minorTickPosition': 'inside',
            'minorGridLineWidth': 0,
            'minorTickColor': '#666',

            'tickInterval': 1,
            'tickWidth': 2,
            'tickPosition': 'inside',
            'tickLength': 10,
            'tickColor': '#666',
        }

        self.g.tooltip.formatter = 'function() { return this.series.chart.tooltipText; }'

        self.g.exporting.enabled = False

        self.g.series = [{
            'data': [{
                'id': 'hour',
                'y': '(function() { var now = new Date(); return now.getHours() + now.getMinutes() / 60; })()',
                'dial': {
                    'radius': '60%',
                    'baseWidth': 4,
                    'baseLength': '95%',
                    'rearLength': 0
                }
            }, {
                'id': 'minute',
                'y': '(function() { var now = new Date(); return now.getMinutes() * 12 / 60 + now.getSeconds() * 12 / 3600; })()',
                'dial': {
                    'baseLength': '95%',
                    'rearLength': 0
                }
            }, {
                'id': 'second',
                'y': '(function() { var now = new Date(); return now.getSeconds() * 12 / 60; })()',
                'dial': {
                    'radius': '100%',
                    'baseWidth': 1,
                    'rearLength': '20%'
                }
            }],
            'animation': False,
            'dataLabels': {
                'enabled': False
            }
        }]



    def _repr_html_(self):
        return self.g.html(js_extra=self.js_extra, callback=self.callback)



