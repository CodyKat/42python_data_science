from load_csv import load


def main():
    """"""
    population_total = load('population_total.csv')
    row = population_total[population_total['country'] == 'Souch Korea']

if __name__ == "__main__":
    main()