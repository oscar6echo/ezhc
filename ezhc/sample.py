
import os
import numpy as np
import pandas as pd

from ._config import SAMPLES_DIR, DF_ONE_IDX_SEVERAL_COL, DF_ONE_IDX_SEVERAL_COL_2, \
                    DF_ONE_IDX_ONE_COL, DF_ONE_IDX_TWO_COL, DF_TWO_IDX_ONE_COL, DF_SCATTER, \
                    DF_BUBBLE, DF_HEATMAP, DF_SEVERAL_IDX_ONE_COL, DF_SEVERAL_IDX_ONE_COL_2, \
                    DF_TWO_IDX_SEVERAL_COL


def load_df(src):
    _dir = os.path.dirname(__file__)
    df_file = os.path.join(_dir, SAMPLES_DIR, src)
    df = pd.read_csv(df_file)
    return df


def df_timeseries(N=3, Nb_bd=500, seed=123456):
    np.random.seed(seed)

    rate = 0.02
    vol = 0.25
    dt = 1.0/260
    tracks = np.zeros([Nb_bd, N], dtype=np.float)

    for k in range(N):
        ln_returns = (rate-vol**2/2)*dt+vol*np.sqrt(dt)*np.random.normal(size=Nb_bd)
        ln_returns[0] = 0.0
        tracks[:, k] = np.exp(ln_returns).cumprod()

    dates = pd.date_range(start=pd.datetime(2015, 1, 1), periods=Nb_bd, freq='B')
    df = pd.DataFrame(data=tracks, index=dates, columns=['Track'+str(1+i) for i in range(N)])

    return df


def df_one_idx_several_col():
    df = load_df(DF_ONE_IDX_SEVERAL_COL)
    df = df.set_index('Fruit')
    return df


def df_one_idx_several_col_2():
    df = load_df(DF_ONE_IDX_SEVERAL_COL_2)
    df = df.set_index('WeekDay')
    return df


def df_one_idx_one_col():
    df = load_df(DF_ONE_IDX_ONE_COL)
    df = df.set_index('Brand')
    return df


def df_one_idx_two_col():
    df = load_df(DF_ONE_IDX_TWO_COL)
    df = df.set_index('Month')
    return df


def df_two_idx_one_col():
    df = load_df(DF_TWO_IDX_ONE_COL)
    df = df.set_index(['Brand', 'Version'])
    return df


def df_scatter():
    df = load_df(DF_SCATTER)
    df = df.set_index(['Height', 'Weight'])
    return df


def df_bubble():
    df = load_df(DF_BUBBLE)
    df = df.set_index(['Cat', 'x', 'y'])
    return df


def df_heatmap():
    df = load_df(DF_HEATMAP)
    df = df.set_index(['Name', 'Day'])
    return df


def df_several_idx_one_col():
    df = load_df(DF_SEVERAL_IDX_ONE_COL)
    df = df.set_index(['Region', 'Country', 'Cause'])
    df = df.sort_index()
    return df

def df_several_idx_one_col_2():
    df = load_df(DF_SEVERAL_IDX_ONE_COL_2)
    df = df.set_index(['Continent', 'Region', 'Country'])
    df = df.sort_index()
    return df


def df_two_idx_several_col():
    df = load_df(DF_TWO_IDX_SEVERAL_COL)
    df = df.set_index(['Strategy', 'Ticker'])
    df = df.sort_index()
    return df
