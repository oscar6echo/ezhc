
import os
import uuid
import pandas as pd
import datetime as dt
from IPython.display import HTML
from copy import deepcopy as copy

from ._config import JS_LIBS_ONE, JS_LIBS_TWO, JS_SAVE
from ._hc_versions import get_hc_versions
from .scripts import JS_JSON_PARSE


def opt_to_dict(options, chart_id='chart_id'):
    """
    returns dictionary of options for highcharts/highstocks object
    with field chart:renderTo set to arg chart_id
    """

    _options = dict(options)
    _options['chart']['renderTo'] = chart_id
    return _options


def opt_to_json(options, chart_id='chart_id', save=False, save_name=None, save_path='saved'):
    """
    returns json of options for highcharts/highstocks object
    """
    def json_dumps(obj):
        return pd.io.json.dumps(obj)

    _options = opt_to_dict(options, chart_id)
    json_options = json_dumps(_options)

    # save
    if save == True:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        tag = save_name if save_name else 'plot'
        with open(os.path.join(save_path, tag + '.json'), 'w') as f:
            f.write(json_options)

    return json_options


def html(
        options, lib='highcharts', dated=True, save=False, save_name=None, save_path='saved',
        notebook=True, html_init=None, js_option_postprocess=None, js_extra=None, callback=None,
        footer=None, version='latest', proxy=None, center=False):
    """
    save=True will create a standalone HTML doc under save_path directory (after creating folder if necessary)
    """

    def json_dumps(obj):
        return pd.io.json.dumps(obj)

    chart_id = str(uuid.uuid4()).replace('-', '_')

    _options = dict(options)
    _options['chart']['renderTo'] = chart_id + 'container_chart'
    json_options = json_dumps(_options).replace('__uuid__', chart_id)

    # HIGHCHARTS VERSION
    hc_versions = get_hc_versions(proxy)
    if version is None:
        v = ''
    elif version == 'latest':
        v = hc_versions[-1] + '/'
    else:
        msg = 'version must be a valid highcharts version - see https://github.com/highcharts/highcharts/releases'
        assert version in hc_versions, msg
        v = version + '/'

    JS_LIBS_ONE_version = copy(JS_LIBS_ONE)
    for k, e in enumerate(JS_LIBS_ONE_version):
        if 'highcharts.com' in e:
            JS_LIBS_ONE_version[k] = e.format(v)

    JS_LIBS_TWO_version = copy(JS_LIBS_TWO)
    for k, e in enumerate(JS_LIBS_TWO_version):
        if 'highcharts.com' in e:
            JS_LIBS_TWO_version[k] = e.format(v)

    # HTML
    if center:
        html = '<div style="text-align:center;"><div id="__uuid__container_chart" style="display: inline-block"></div></div>'
    else:
        html = '<div id="__uuid__container_chart"></div>'

    html_init = html_init if html_init else ''
    if html_init:
        html = html_init + html

    footer = footer if footer else ''
    html = html + footer
    html = html.replace('__uuid__', chart_id)

    # JS
    js_option_postprocess = js_option_postprocess.replace(
        '__uuid__', chart_id) if js_option_postprocess else ''
    js_extra = js_extra if js_extra else ''
    callback = ', ' + \
        callback.replace('__uuid__', chart_id) if callback else ''

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

    if lib == 'highcharts':
        js_call = 'window.chart = new Highcharts.Chart(options%s);' % (
            callback)
    elif lib == 'highstock':
        js_call = 'window.chart = new Highcharts.StockChart(options%s);' % (
            callback)

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

    // hardcoded var - temporary
    require(%s, function(jquery,
                         Highcharts,
                         d3
                         ) {
        // hardcoded var - temporary
        require(%s, function(hcMore,
                             exporting,
                             offLineExporting,
                             exportData,
                             drilldown,
                             heatmap,
                             treemap,
                             sunburst,
                             dataTables,
                             ) {
            hcMore(Highcharts);
            exporting(Highcharts);
            offLineExporting(Highcharts);
            exportData(Highcharts);
            drilldown(Highcharts);
            heatmap(Highcharts);
            treemap(Highcharts);
            sunburst(Highcharts);
            %s
            %s
            %s
            %s
        });
    });
    </script>""" % (JS_LIBS_ONE_version, JS_LIBS_TWO_version,
                    js_option, js_extra, js_call, js_debug)

    # save
    js_load = ''.join(['<script src="%s"></script>' % e for e in JS_SAVE])
    if save == True:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        tag = save_name if save_name else 'plot'
        dated = dt.datetime.now().strftime('_%Y%m%d_%H%M%S') if dated else ''

        with open(os.path.join(save_path, tag + dated + '.html'), 'w') as f:
            f.write(js_load + html + js)

        with open(os.path.join(save_path, tag + dated + '-for-ezdashboard.html'), 'w') as f:
            f.write(html + js)


    if notebook:
        return html + js
    else:
        return js_load + html + js


def plot(
        options, lib='highcharts', dated=True, save=False, save_name=None, save_path='saved',
        notebook=True, html_init=None, js_option_postprocess=None, js_extra=None, callback=None,
        footer=None, version='latest', proxy=None, center=False):
    contents = html(options, lib, dated, save, save_name, save_path, notebook,
                    html_init, js_option_postprocess, js_extra, callback, footer,
                    version, proxy, center)
    return HTML(contents)
