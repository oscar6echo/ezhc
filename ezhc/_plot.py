
import os
import pandas as pd
import datetime as dt
import uuid
from IPython.display import HTML


from _config import JS_LIBS_ONE, JS_LIBS_TWO, JS_SAVE
from scripts import JS_JSON_PARSE




def html(options, lib='hicharts', save=False, js_preprocess=None, callback=None):
    """
    save=True will create a standalone HTML doc under localdir/saved (creating folfer save if necessary)
    """

    def json_dumps(obj):
        return pd.io.json.dumps(obj)


    _options = dict(options)

    def clean_function_str(key, n=10):
        """
        Remove new line characters in the first say 10 characters
        of the value corresponding to key in dictionary _options.
        This value is a string that potentially starts with
        'function' or ' function' or '[newline]function' or '[newline]function', etc
        This cleaning makes js string parsing easier to recognize functions.
        """
        if key in _options.keys():
            new_str = _options[key][:n].replace('\n', '').replace('\r', '') + _options[key][n:]
            _options[key] = new_str


    for k, v in _options.iteritems():
        if isinstance(v, str):
            clean_function_str(k) 


    chart_id = str(uuid.uuid4()).replace('-', '_')
    _options['chart']['renderTo'] = chart_id


    js_init = """
    var options = %s;
    %s
    window.opt = jQuery.extend(true, {}, options);
    console.log('Highcharts/Highstock options accessible as opt');
    """ % (json_dumps(_options), JS_JSON_PARSE) 


    if not js_preprocess:
        js_preprocess = ''


    if callback:
        callback = ', ' + callback
    else:
        callback = ''
    

    if lib=='highcharts':
        js_call = 'new Highcharts.Chart(options%s);' % (callback)
    elif lib=='highstock':
        js_call = 'new Highcharts.StockChart(options%s);' % (callback)


    html = """
    <div id="%s"></div>
    """ % (chart_id)


    js = """<script>
    require(%s, function() {
        require(%s, function() {
            %s
            %s
            %s
        });
    });
    </script>""" % (JS_LIBS_ONE, JS_LIBS_TWO, js_init, js_preprocess, js_call)
    
    if save==True:
        if not os.path.exists('saved'):
            os.makedirs('saved')
        with open(os.path.join('saved', 'plot_'+dt.datetime.now().strftime('%Y%m%d_%H%M%S')+'.html'), 'w') as f:
            contents = """
            <script src="%s"></script>
            <script src="%s"></script>
            %s
            """ % (JS_SAVE[0], JS_SAVE[1], html+js)
            f.write(contents)
    
    return html+js

    



def plot(options, lib='hicharts', save=False, js_preprocess=None, callback=None):
    contents = html(options, lib, save, js_preprocess, callback)
    return HTML(contents)

  

