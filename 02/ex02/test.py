import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# 예제 데이터
data = {
    'Year': [1800, 1840, 1880, 1920, 1960, 2000, 2040],
    'Belgium': [5e6, 6e6, 7e6, 8e6, 9e6, 9.5e6, 9.8e6],
    'France': [20e6, 25e6, 30e6, 35e6, 40e6, 55e6, 60e6]
}
df = pd.DataFrame(data)

def millions_formatter(x, pos):
    return f'{int(x/1e6)}M'

formatter = FuncFormatter(millions_formatter)

ax = df.plot(x='Year', y=['Belgium', 'France'])
ax.yaxis.set_major_formatter(formatter)

plt.ylabel('Population')
plt.title('Population Projections')
plt.show()
