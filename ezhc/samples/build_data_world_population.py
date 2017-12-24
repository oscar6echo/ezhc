import os
import pandas as pd

from data_population import data


dfd = pd.DataFrame(data)

dic_1 = dfd[dfd['id'].str.startswith(
    '1')][['id', 'name']].set_index('id').to_dict()['name']
dic_2 = dfd[dfd['id'].str.startswith(
    '2')][['id', 'name']].set_index('id').to_dict()['name']
dic_3 = dfd[dfd['id'].str.startswith(
    '3')][['id', 'name']].set_index('id').to_dict()['name']

g = dfd.groupby('parent')

dic_tree_1 = {}
dic_tree_2 = {}
for k, v in g.groups.items():
    if k.startswith('1'):
        df = g.get_group(k)
        dic_tree_1[dic_1[k]] = list(df['name'])
    if k.startswith('2'):
        df = g.get_group(k)
        dic_tree_2[dic_2[k]] = list(df['name'])

g = dfd.groupby('id')
dic_val = {}
for k, v in g.groups.items():
    if k.startswith('3'):
        df = g.get_group(k)
        dic_val[dic_3[k]] = df['value'].iloc[0]

data = []
for continent, li_reg in dic_tree_1.items():
    for reg in li_reg:
        li_country = dic_tree_2[reg]
        for country in li_country:
            v = dic_val[country]
            data.append([continent, reg, country, v])

dfs = pd.DataFrame(data=data,
                   columns=['Continent', 'Region', 'Country', 'Population'])
dfs = dfs.set_index(['Continent', 'Region', 'Country'])

path = 'df_several_idx_one_col_2.csv'
dfs.to_csv(path)
