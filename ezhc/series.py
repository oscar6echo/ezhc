
import pandas as pd



def series(df, options, *args, **kwargs):
    idx = df.index
    col = df.columns
    data = df.values
    assert(isinstance(idx, pd.core.index.Index))
    
    series = []
    for k, c in enumerate(col):
        if df[c].dtype.kind in 'fib':
            v = data[:, k]
            sec = c in kwargs.get('secondary_y', [])
            d = {
                'name': c if not sec else c + ' (right)',
                'yAxis': int(sec),
                'data': [[idx[q], v[q]] for q in range(len(v))],             
            }
            if c in kwargs.get('color', []):
                d['color'] = kwargs['color'].get(c)
            if kwargs.get('dashStyle', []):
                d['dashStyle'] = kwargs['dashStyle'].get(c, 'Solid')
            series.append(d)
    return series




def series_drilldown(df, options, *args, **kwargs):
    idx = df.index
    col = df.columns
    assert(isinstance(idx, pd.core.index.MultiIndex))
    assert(len(idx.levshape)==2)
    assert(len(col)==1)
    assert(df[col[0]].dtype.kind in 'if')
    
    levone = list(idx.levels[0])
    data = []
    drilldownSeries = []
    for c in levone:
        dfs = df.xs(c)
        ii = dfs.index.values.flatten()
        vv = dfs.values.flatten()
        
        d1 = {
            'name': c,
            'y': dfs.sum().values[0],
            'drilldown': c if len(dfs)>1 else None,
        }
        data.append(d1)

        if len(dfs)>1:
            d2 = {
                'name': c,
                'data': [[str(ii[q]), vv[q]] for q in range(len(ii))],
                'id': c,                
            }
            drilldownSeries.append(d2)

    series = [{'name': col[0],'data': data, 'colorByPoint': True}]
    return series, drilldownSeries






def series_scatter(df, options, *args, **kwargs):
    idx = df.index
    col = df.columns
    assert(isinstance(idx, pd.core.index.MultiIndex))
    assert(len(idx.levshape)==2)
    assert(len(col)==1)
    assert(df[col[0]].dtype.kind in 'iO')
        
    data = df.values.flatten()
    elmt = list(set(data))
    color = kwargs.get('color', {})
    series = []
    
    for e in elmt:
        dfs = df[df.iloc[:, 0]==e]
        idx = dfs.index
        series.append({'animation': False,
                       'name': e,
                       'color': color.get(e, None),
                       'data': [[idx[k][0], idx[k][1]] for k in range(len(dfs))],
                      })
    return series







def series_bubble(df, options, *args, **kwargs):
    idx = df.index
    col = df.columns
    assert(isinstance(idx, pd.core.index.MultiIndex))
    assert(len(idx.levshape)==3)
    assert(len(col)==1)
    assert(df[col[0]].dtype.kind in 'fib')

    names = list(idx.levels[0])
    color = kwargs.get('color', {})
    series = []
    for s in names:
        dfs = df.xs(s)
        v = dfs.values.flatten()
        idxs = dfs.index
        d = {
            'name': s,
            'data': [[idxs[q][0], idxs[q][1], v[q]] for q in range(len(v))],             
        }
        if s in kwargs.get('color', []):
            d['color'] = kwargs['color'].get(s)

        series.append(d)
        
    return series
    



def series_treemap(df, options, *args, **kwargs):
    idx = df.index
    col = df.columns
    assert(isinstance(idx, pd.core.index.MultiIndex))
    assert(df[col[0]].dtype.kind in 'fi')
        
    data = df.values
    elmt = list(set(data))
    color = kwargs.get('color', {})
    series = []
    
    for e in elmt:
        dfs = df[df.iloc[:, 0]==e]
        idx = dfs.index
        series.append({'animation': False,
                       'name': e,
                       'color': color.get(e, None),
                       'data': [[idx[k][0], idx[k][1]] for k in range(len(dfs))],
                      })
    return series



