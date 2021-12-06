
import pandas as pd

DEFAULT_COLORS = ["#7cb5ec", "#434348", "#90ed7d", "#f7a35c", "#8085e9",
                  "#f15c80", "#e4d354", "#2b908f", "#f45b5b", "#91e8e1"]


def series(df, *args, **kwargs):
    idx = df.index
    col = df.columns
    data = df.values
    assert(isinstance(idx, pd.Index))

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
            for key in kwargs.keys():
                if key == 'fillColor':
                    d['type'] = 'area'
                    d['fillColor'] = kwargs['fillColor'].get(c)
                elif c in kwargs.get(key, []):
                    d[key] = kwargs[key].get(c)
            series.append(d)
    return series


def series_range(df, *args, **kwargs):
    idx = df.index
    col = df.columns
    data = df.values
    assert(isinstance(idx, pd.Index))
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


def series_drilldown_orig(df, colorByPoint=True, pointPlacement='on', *args, **kwargs):
    idx = df.index
    col = df.columns
    assert(isinstance(idx, pd.MultiIndex))
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


def series_drilldown(df,
                     top_name='Top',
                     colorByPoint=True,
                     pointPlacement='on',
                     set_color=False,
                     colors=None,
                     set_precision=False,
                     precision=None,
                     *args,
                     **kwargs):
    idx = df.index
    col = df.columns
    assert(isinstance(idx, pd.MultiIndex))
    for c in col:
        assert df[c].dtype.kind in 'if'

    class DrillDownBuilder:
        """
        Recursive build of drilldown structure
        """

        def __init__(self,
                     df,
                     top_name='Top',
                     colorByPoint=True,
                     pointPlacement='on',
                     set_color=False,
                     colors=None,
                     set_precision=False,
                     precision=None):

            self.top_name = top_name
            self.colorByPoint = colorByPoint
            self.pointPlacement = pointPlacement
            self.df = df
            self.set_color = set_color
            self.colors = colors
            self.set_precision = set_precision
            self.precision = precision

            self.items = []
            self.top_item = self.build(df)

        def build(self, dfxs, parent=None, name=None):
            top_items = []
            for col in dfxs.columns:
                dfc = dfxs[[col]]
                item = {
                    'id': col + '-toplevel',
                    'name': dfc.columns[0]
                }
                if len(dfxs.columns) == 1:
                    item['name'] = self.top_name
                if parent:
                    item['id'] = str(parent) + '-' + name
                    item['name'] = name
                if self.colorByPoint:
                    item['colorByPoint'] = self.colorByPoint

                data = []

                idx = dfc.index
                if isinstance(idx, pd.MultiIndex):

                    for k, idx0 in enumerate(idx.levels[0]):
                        df_sub = dfc.xs(idx0)
                        total = df_sub.sum()[0]
                        d = {
                            'name': str(idx0),
                            'y': total,
                            'drilldown': item['id'] + '-' + str(idx0)
                        }
                        if self.pointPlacement:
                            d['pointPlacement'] = self.pointPlacement
                        if self.set_precision:
                            d['y'] = round(total, self.precision)
                        if self.set_color:
                            d['color'] = self.colors[k % len(self.colors)]
                        data.append(d)

                        self.build(df_sub,
                                   parent=item['id'],
                                   name=str(idx0))

                elif isinstance(idx, pd.Index):

                    for k, idx0 in enumerate(idx):
                        df_sub = dfc.xs(idx0)
                        total = df_sub.sum()
                        d = {
                            'name': str(idx0),
                            'y': total,
                        }
                        if self.set_precision:
                            d['y'] = round(total, self.precision)
                        if self.set_color:
                            d['color'] = self.colors[k % len(self.colors)]
                        data.append(d)

                else:
                    raise Exception('Pandas Index Unknown Problem')

                item['data'] = data
                self.items.append(item)
                top_items.append(item)

            return top_items

        def series(self):
            return self.top_item

        def drilldown_series(self):
            return self.items

    dd = DrillDownBuilder(df,
                          top_name=top_name,
                          colorByPoint=colorByPoint,
                          pointPlacement=pointPlacement,
                          set_color=set_color,
                          colors=colors,
                          set_precision=set_precision,
                          precision=precision)

    return dd.series(), dd.drilldown_series()


# def series_drilldown_orig(df, colorByPoint=True, pointPlacement='on', *args, **kwargs):
#     idx = df.index
#     col = df.columns
#     assert(isinstance(idx, pd.MultiIndex))
#     assert(len(idx.levshape) == 2)
#     for c in col:
#         assert df[c].dtype.kind in 'if'

#     levone = list(idx.levels[0])
#     data = []
#     series = []
#     drilldownSeries = []
#     for co in col:
#         data = []
#         for c in levone:
#             dfs = df.xs(c)
#             ii = dfs[[co]].index.values.flatten()
#             vv = dfs[[co]].values.flatten()

#             d1 = {
#                 'name': c,
#                 'y': dfs[[co]].sum().values[0],
#                 'drilldown': c + ' - ' + co if len(dfs) > 1 else None,
#                 'pointPlacement': pointPlacement
#             }
#             if co in kwargs.get('color', []):
#                 d1['color'] = kwargs['color'].get(co)
#             data.append(d1)

#             if len(dfs) > 1:
#                 d2 = {
#                     'name': c + ' - ' + co,
#                     'data': [[str(ii[q]), vv[q]] for q in range(len(ii))],
#                     'id': c + ' - ' + co,
#                     'pointPlacement': pointPlacement
#                 }
#                 drilldownSeries.append(d2)

#         s = {'name': co, 'data': data, 'colorByPoint': colorByPoint}
#         if co in kwargs.get('color', []):
#             s['color'] = kwargs['color'].get(co)
#         series.append(s)

#     return series, drilldownSeries


def series_scatter(df, color_column=None, title_column=None, *args, **kwargs):
    idx = df.index
    col = df.columns
    assert(isinstance(idx, pd.MultiIndex))
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
    assert(isinstance(idx, pd.MultiIndex))
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
    assert(isinstance(idx, pd.Index))
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
        """
        Recursive build of tree data structure
        """

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
