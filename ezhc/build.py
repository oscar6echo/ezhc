
import pandas as pd


def series(df, *args, **kwargs):
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
            if c in kwargs.get('fillColor', []):
                d['type'] = 'area'
                d['fillColor'] = kwargs['fillColor'].get(c)
            if c in kwargs.get('lineColor', []):
                d['lineColor'] = kwargs['lineColor'].get(c)
            if kwargs.get('dashStyle', []):
                d['dashStyle'] = kwargs['dashStyle'].get(c, 'Solid')
            series.append(d)
    return series


def series_range(df, *args, **kwargs):
    idx = df.index
    col = df.columns
    data = df.values
    assert(isinstance(idx, pd.core.index.Index))
    assert(len(col) == 2)
    assert(df[col[0]].dtype.kind in 'if')
    assert(df[col[1]].dtype.kind in 'if')

    series = [{
        'data': [[data[q, 0], data[q, 1]] for q in range(data.shape[0])],
    }]
    if 'color' in kwargs:
        series['color'] = kwargs['color']
    axis_categories = list(idx)

    return axis_categories, series


def series_drilldown(df, colorByPoint=True, pointPlacement='on', *args, **kwargs):
    idx = df.index
    col = df.columns
    assert(isinstance(idx, pd.core.index.MultiIndex))
    assert(len(idx.levshape) == 2)
    for c in col:
        assert df[c].dtype.kind in 'if'

    levone = list(idx.levels[0])
    data = []
    series = []
    drilldownSeries = []
    for co in col:
        data = []
        for c in levone:
            dfs = df.xs(c)
            ii = dfs[[co]].index.values.flatten()
            vv = dfs[[co]].values.flatten()

            d1 = {
                'name': c,
                'y': dfs[[co]].sum().values[0],
                'drilldown': c+' - '+co if len(dfs) > 1 else None,
                'pointPlacement': pointPlacement
            }
            if co in kwargs.get('color', []):
                d1['color'] = kwargs['color'].get(co)
            data.append(d1)

            if len(dfs) > 1:
                d2 = {
                    'name': c+' - '+co,
                    'data': [[str(ii[q]), vv[q]] for q in range(len(ii))],
                    'id': c+' - '+co,
                    'pointPlacement': pointPlacement
                }
                drilldownSeries.append(d2)

        s = {'name': co, 'data': data, 'colorByPoint': colorByPoint}
        if co in kwargs.get('color', []):
            s['color'] = kwargs['color'].get(co)
        series.append(s)

    return series, drilldownSeries


def series_scatter(df, *args, **kwargs):
    idx = df.index
    col = df.columns
    assert(isinstance(idx, pd.core.index.MultiIndex))
    assert(len(idx.levshape) == 2)
    assert(len(col) == 1)
    assert(df[col[0]].dtype.kind in 'iO')

    data = df.values.flatten()
    elmt = list(set(data))
    color = kwargs.get('color', {})
    series = []

    for e in elmt:
        dfs = df[df.iloc[:, 0] == e]
        idx = dfs.index
        series.append({'animation': False,
                       'name': e,
                       'color': color.get(e, None),
                       'data': [[idx[k][0], idx[k][1]] for k in range(len(dfs))],
                    })
    return series


def series_bubble(df, *args, **kwargs):
    idx = df.index
    col = df.columns
    assert(isinstance(idx, pd.core.index.MultiIndex))
    assert(len(idx.levshape) == 3)
    assert(len(col) == 1)
    assert(df[col[0]].dtype.kind in 'fib')

    names = list(idx.levels[0])
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


def series_treemap(df, *args, **kwargs):
    idx = df.index
    col = df.columns
    assert(isinstance(idx, pd.core.index.MultiIndex))
    assert(len(col) == 1)

    data = df.values
    elmt = list(set(data))
    color = kwargs.get('color', {})
    series = []

    for e in elmt:
        dfs = df[df.iloc[:, 0] == e]
        idx = dfs.index
        series.append({
            'animation': False,
            'name': e,
            'color': color.get(e, None),
            'data': [[idx[k][0], idx[k][1]] for k in range(len(dfs))],
        })
    return series
    pass


def series_heatmap(df, *args, **kwargs):
    idx = df.index
    col = df.columns
    assert(isinstance(idx, pd.core.index.Index))
    for c in col:
        assert(df[c].dtype.kind in 'if')

    dft = df.copy()
    dft.index = range(len(df.index))
    dft.columns = range(len(df.columns))
    res_data = list(dft.stack().swaplevel(0, 1).reset_index().values)
    res_idx = list(df.columns)
    res_col = list(df.index)

    return res_idx, res_col, res_data
