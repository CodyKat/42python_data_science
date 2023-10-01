from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Show graph south korea life expectancy."""
    csv_file = load('life_expectancy_years.csv')
    row = csv_file[csv_file['country'] == 'South Korea']
    col = row.drop(columns=['country']).T
    col = col.rename(columns={col.columns[0]:'South Korea'})
    col.plot(xlabel='Year', ylabel='Life expectancy')
    plt.title('South Korea Life expectancy Projections')
    plt.show()


if __name__ == "__main__":
    main()