import pandas as pd
import matplotlib.pyplot as plt

def make_sliding_time_windows(df, steps_back, col_name='mean_event'):
    ret = df.copy()
    for i in range(1, steps_back + 1):
        ret['{}_{}'.format(col_name, i)] = ret[col_name].shift(i)
    return ret


def remove_multi_index(df):
    ret = df.copy()
    ret.columns = ret.columns.droplevel()
    return ret

def plot_clipped(df):
    fig, ax = plt.subplots()
    df.iloc[:,:3].plot(ax=ax, color=['C0','C1','C2'], linewidth=1, linestyle='--')
    df.iloc[:,3:].plot(ax=ax, color=['C0','C1','C2'])
    plt.show()