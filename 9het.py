import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
filename = 'BRK-B (1).csv'
df = pd.read_csv(filename)
df['ret_log'] = np.log(df['Adj Close']/df['Adj Close'].shift(1))

df.index = pd.to_datetime(df['Date'])
df['ret_log'].plot()

plt.show()
print(1)
