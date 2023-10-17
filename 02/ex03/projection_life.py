from load_csv import load
from matplotlib import pyplot as plt

def kilos(x, pos):
    """The two arguments are the value and tick position."""
    return f'{x*1e-3:1.0f}K'

def main():
    """draw scatter from life_expectancy and income per poerson in 1900"""
    income_per_persion = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    life_expectancy = load('life_expectancy_years.csv')

    income_per_persion_1900 = income_per_persion['1900']
    print(type(income_per_persion_1900))
    # income_per_persion_1900 = income_per_persion_1900.replace('K', 'e3')
    print(income_per_persion_1900)
    life_expectancy_1900 = life_expectancy['1900']

    ax = plt.subplot()
    plt.scatter(income_per_persion_1900, life_expectancy_1900)
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.xscale('log')
    plt.title('1900')
    ax.xaxis.set_major_formatter(kilos)
    plt.show()

if __name__ == "__main__":
    main()