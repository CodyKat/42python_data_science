from matplotlib import pyplot as plt
from load_csv import load


def main():
    """"""
    population_total = load('population_total.csv')
    countrys = population_total['country']
    selected_row = population_total.loc[
        (population_total['country'] == 'South Korea') |
        (population_total['country'] == 'France')
        ]
    selected_row = selected_row.T
    selected_row = selected_row.loc[selected_row['country']]
    print(selected_row)
    # selected_row = selected_row.drop(index=1)
    # print(selected_row)
    # selected_row.plot()
    # plt.show()
    # two_countries = population_total.loc()
if __name__ == "__main__":
    main()