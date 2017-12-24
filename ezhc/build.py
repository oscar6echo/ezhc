
import pandas as pd

DEFAULT_COLORS = ["#7cb5ec", "#434348", "#90ed7d", "#f7a35c", "#8085e9",
                  "#f15c80", "#e4d354", "#2b908f", "#f45b5b", "#91e8e1"]


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
                'drilldown': c + ' - ' + co if len(dfs) > 1 else None,
                'pointPlacement': pointPlacement
            }
            if co in kwargs.get('color', []):
                d1['color'] = kwargs['color'].get(co)
            data.append(d1)

            if len(dfs) > 1:
                d2 = {
                    'name': c + ' - ' + co,
                    'data': [[str(ii[q]), vv[q]] for q in range(len(ii))],
                    'id': c + ' - ' + co,
                    'pointPlacement': pointPlacement
                }
                drilldownSeries.append(d2)

        s = {'name': co, 'data': data, 'colorByPoint': colorByPoint}
        if co in kwargs.get('color', []):
            s['color'] = kwargs['color'].get(co)
        series.append(s)

    return series, drilldownSeries


def series_scatter(df, color_column=None, title_column=None, *args, **kwargs):
    idx = df.index
    col = df.columns
    assert(isinstance(idx, pd.core.index.MultiIndex))
    assert(len(idx.levshape) == 2)
    assert(len(col) <= 2)
    assert(df[color_column].dtype.kind in 'iO')

    if color_column == None:
        assert(len(col) == 1)
        color_column = col[0]
    if title_column == None:
        title_column = color_column

    data = df[[color_column]].values.flatten()
    elmt = list(set(data))
    color = kwargs.get('color', {})
    series = []

    for e in elmt:
        dfs = df[df[color_column] == e]
        idx = dfs.index
        names = list(dfs[title_column])
        series.append({'animation': False,
                       'name': e,
                       'turboThreshold': 0,
                       'color': color.get(e, None),
                       'data': [{'x': idx[k][0], 'y': idx[k][1], 'name': str(names[k])}
                                for k in range(len(dfs))],
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


def series_tree(df,
                set_total=False,
                name_total='All',
                set_color=False,
                colors=DEFAULT_COLORS,
                set_value=True,
                precision=2):

    class TreeBuilder:

        def __init__(self,
                     df,
                     set_total,
                     name_total,
                     set_color,
                     colors,
                     set_value,
                     precision):
            self.df = df
            self.set_color = set_color
            self.colors = colors
            self.set_value = set_value
            self.precision = precision

            self.points = []
            if set_total:
                point = {'id': '0',
                         'name': name_total,
                         }
                if set_value:
                    point['value'] = round(df.sum().sum(), precision)
                self.points.append(point)
                total = self.build(df, parent='0')
            else:
                total = self.build(df)

        def build(self, dfxs, parent=None):
            idx = dfxs.index
            sum_value = 0

            if isinstance(idx, pd.MultiIndex):
                for k, name in enumerate(idx.levels[0]):
                    point = {
                        'name': name,
                    }
                    if parent:
                        point['id'] = parent + '.' + str(k)
                        point['parent'] = parent
                    else:
                        point['id'] = '0.' + str(k)
                        if self.set_color:
                            point['color'] = self.colors[k % len(self.colors)]

                    df_sub = dfxs.xs(name)
                    df_sub = df_sub.reset_index().set_index(df_sub.index.names)

                    value = self.build(df_sub,
                                       parent=point.get('id'))
                    sum_value += value
                    if self.set_value:
                        point['value'] = round(value, self.precision)
                    self.points.append(point)

            elif isinstance(idx, pd.Index):

                for k, name in enumerate(idx):
                    value = dfxs.loc[name][0]
                    sum_value += value

                    point = {
                        'name': name,
                        'value': round(value, self.precision)
                    }
                    if parent:
                        point['id'] = parent + '.' + str(k)
                        point['parent'] = parent
                    else:
                        point['id'] = 'id_' + str(k)
                        point['color'] = self.colors[k % len(self.colors)]

                    self.points.append(point)

            else:
                raise Exception('Pandas Index Unknown Problem')

            return sum_value

    col = df.columns
    assert(len(col) == 1)
    tb = TreeBuilder(df,
                     set_total,
                     name_total,
                     set_color,
                     colors,
                     set_value,
                     precision)
    return tb.points
