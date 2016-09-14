
import os
import pandas as pd
import datetime as dt
import uuid
from IPython.display import HTML


from ._config import JS_LIBS_ONE, JS_LIBS_TWO, JS_SAVE
from .scripts import JS_JSON_PARSE



def html(options, lib='hicharts', dated=True, save=False, save_name=None,
         html_init=None, js_option_postprocess=None, js_extra=None, callback=None, footer=None):
    """
    save=True will create a standalone HTML doc under localdir/saved (creating folfer save if necessary)
    """

    def json_dumps(obj):
        return pd.io.json.dumps(obj)


    chart_id = str(uuid.uuid4()).replace('-', '_')

    _options = dict(options)
    _options['chart']['renderTo'] = chart_id+'container_chart'
    json_options = json_dumps(_options).replace('__uuid__', chart_id)


    # HTML
    html_init = html_init if html_init else '<div id="__uuid__"><div id="__uuid__container_chart"></div></div>'
    footer = footer if footer else ''

    html = html_init + footer
    html = html.replace('__uuid__', chart_id)


    # JS
    js_option_postprocess = js_option_postprocess.replace('__uuid__', chart_id) if js_option_postprocess else ''
    js_extra = js_extra if js_extra else ''
    callback = ', '+callback.replace('__uuid__', chart_id) if callback else ''

    js_option = """
    var options = %s;
    %s
    %s

    var opt = $.extend(true, {}, options);
    if (window.opts==undefined) {
        window.opts = {};
    }
    window.opts['__uuid__'] = opt;

    console.log('Highcharts/Highstock options accessible as opts["__uuid__"]');
    """.replace('__uuid__', chart_id) % (json_options, JS_JSON_PARSE, js_option_postprocess)


    if lib=='highcharts':
        js_call = 'window.chart = new Highcharts.Chart(options%s);' % (callback)
    elif lib=='highstock':
        js_call = 'window.chart = new Highcharts.StockChart(options%s);' % (callback)

    js_debug = """
    console.log('Highcharts/Highstock chart accessible as charts["__uuid__"]');
    """.replace('__uuid__', chart_id)

    js = """<script>
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
            %s
        });
    });
    </script>""" % (JS_LIBS_ONE, JS_LIBS_TWO, js_option, js_extra, js_call, js_debug)

    # save
    if save==True:
        if not os.path.exists('saved'):
            os.makedirs('saved')
        tag = save_name if save_name else 'plot'
        dated = dt.datetime.now().strftime('_%Y%m%d_%H%M%S') if dated else ''
        with open(os.path.join('saved', tag+dated+'.html'), 'w') as f:
            js_load = ''.join(['<script src="%s"></script>' % e for e in JS_SAVE])
            contents = js_load+html+js
            f.write(contents)

    return html+js





def plot(options, lib='hicharts', dated=True, save=False, save_name=None,
         html_init=None, js_option_postprocess=None, js_extra=None, callback=None, footer=None):
    contents = html(options, lib, dated, save, save_name, html_init, js_option_postprocess, js_extra, callback, footer)
    return HTML(contents)
