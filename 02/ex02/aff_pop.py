from matplotlib import pyplot as plt
from load_csv import load
import pandas as pd

def main():
    """"""
    population_total = load('population_total.csv')
    korean_row = population_total.loc[population_total['country'] == 'South Korea']
    france_row = population_total.loc[population_total['country'] == 'France']
    korean_row = korean_row.rename(index={95:'South Korea'})
    france_row = france_row.rename(index={58:'France'})
    korean_col = korean_row.drop(columns=['country']).T
    france_col = france_row.drop(columns=['country']).T
    # make 10.0M to 10000000
    korean_col = korean_col.apply(lambda x: x.replace('M', ''))
    korean_col = korean_col.apply(lambda x: float(x) * 1000000)
    print(korean_col)


if __name__ == "__main__":
    main()