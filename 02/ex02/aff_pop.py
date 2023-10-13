from matplotlib import axis, pyplot as plt
from load_csv import load
import pandas as pd
import numpy as np

def millions(x, pos):
    """The two arguments are the value and tick position."""
    return f'{x*1e-6:1.0f}M'

def main():
    """"""
    population_total = load('population_total.csv')
    population_total.set_index(population_total['country'], inplace=True)
    korean_row = population_total.T['South Korea'][1:251]
    france_row = population_total.T['France'][1:251]

    korean_row = korean_row.str.replace('M', 'e6')
    france_row = france_row.str.replace('M', 'e6')
    korean_row = korean_row.astype(float)
    france_row = france_row.astype(float)

    ax = plt.subplot()
    plt.plot(korean_row, label='korean')
    plt.plot(france_row, label='france')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend(loc='lower right')
    plt.xticks(plt.xticks()[0][::40])
    plt.yticks([0, 20e6, 40e6, 60e6])
    ax.yaxis.set_major_formatter(millions)

    plt.show()

if __name__ == "__main__":
    main()