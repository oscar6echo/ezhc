
import json
import pandas as pd

from IPython.display import display, Javascript, Markdown

from ._config import JS_LIBS_ONE, JS_LIBS_TWO, JS_SAVE
from .scripts import JS_JSON_PARSE


class GlobalOptions:
    """
    Used to pass global options to Highcharts object

    API: https://api.highcharts.com/highcharts
    Demos: https://www.highcharts.com/demo
    """

    def __init__(self, data):
        self.options = data
        self.js = None

    def _json_dumps(self, obj):
        return pd.io.json.dumps(obj)

    def create(self):

        if isinstance(self.options, dict):
            json_options = self._json_dumps(self.options)
        else:
            json_options = self.options

        js_default = """
        if (window.HCDefaults == undefined) {
            window.HCDefaults = $.extend(true, {}, Highcharts.getOptions(), {});
            console.log('Highcharts global default options accessible as HCDefaults');
        }
        """

        js_option = """
        var options = %s;
        %s
        window.globalOptions = $.extend(true, {}, options);
        console.log(globalOptions);
        if (window.globalOptions == undefined) {
            window.globalOptions = {};
        }

        console.log('Highcharts global options accessible as globalOptions');
        """ % (json_options, JS_JSON_PARSE)

        js_call = 'Highcharts.setOptions(options);'

        js = """
        // the Jupyter notebook loads jquery.min.js  and require.js and at the top of the page
        // then to make jquery available inside a require module
        // the trick is http://www.manuel-strehl.de/dev/load_jquery_before_requirejs.en.html
        define('jquery', [], function() {
            return jQuery;
        });

        require(%s, function() {
            require(%s, function() {
                %s
                %s
                %s
            });
        });
        """ % (JS_LIBS_ONE, JS_LIBS_TWO, js_default, js_option, js_call)

        return js

    def inject(self, verbose=False):
        if not self.js:
            self.js = self.create()
        if verbose:
            md = """
Highcharts **global options** set in this cell:  
```json
{}
```
""".format(self._json_dumps(self.options))
            display(Markdown(md))
        display(Javascript(self.js))

    def reset(self, verbose=False):
        js_reset = """
        let ResetOptions = function() {
            if (window.HCDefaults){
                var defaultOptions = Highcharts.getOptions();
                for (var prop in defaultOptions) {
                    if (typeof defaultOptions[prop] !== 'function') {
                        delete defaultOptions[prop]
                    }
                    else {
                        console.log(prop);
                    };
                }
                Highcharts.setOptions(window.HCDefaults);
                console.log('Highcharts global options reset to default ie HCDefaults');
            }
        }
        ResetOptions();
        """

        if verbose:
            md = """
Highcharts **global options** reset to default.  
"""
            display(Markdown(md))
        display(Javascript(js_reset))
