from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Show graph south korea life expectancy."""
    csv_file = load('life_expectancy_years.csv')
    my_col = csv_file.loc[csv_file['country'] == 'South Korea']
    my_col = my_col.rename(index={94:'South Korea'})
    my_col = my_col.drop(columns=['country']).T
    my_col.plot(xlabel='Year', ylabel='Life expectancy')
    print(my_col)
    plt.title('South Korea Life expectancy Projections')
    plt.show()


if __name__ == "__main__":
    main()