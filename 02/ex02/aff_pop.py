from matplotlib import pyplot as plt
from load_csv import load


def main():
    """"""
    population_total = load('population_total.csv')
    countrys = population_total['country']
    korean_row = population_total.loc[population_total['country'] == 'South Korea']
    france_row = population_total.loc[population_total['country'] == 'France']
    korean_row = korean_row.rename(index={95:'South Korea'})
    france_row = france_row.rename(index={58:'France'})
    korean_col = korean_row.drop(columns=['country']).T
    france_col = france_row.drop(columns=['country']).T
    numeric_korean_col = []
    numeric_france_col = []
    for i in korean_col['South Korea']:
        numeric_korean_col.append(float(i.replace('M', '')) * 1000000)
    korean_col['South Korea'] = numeric_korean_col
    for i in france_col['France']:
        numeric_france_col.append(float(i.replace('M', '')) * 1000000)
    france_col['France'] = numeric_france_col
    plt.plot(korean_col, 'r', france_col, 'g')
    plt.xlabel = 'Year'
    plt.ylabel = 'Population'
    plt.show()

if __name__ == "__main__":
    main()