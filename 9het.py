import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
filename = 'BRK-B (1).csv'
df = pd.read_csv(filename)
df['ret_log'] = np.log(df['Adj Close']/df['Adj Close'].shift(1))

df.index = pd.to_datetime(df['Date'])
t_day_in_year = 252

df['vol_rolling_1y']=df['ret_log'].rolling(252).std()
df['vol_rolling_2y']=df['ret_log'].rolling(504).std()

df[['vol_rolling_1y', 'vol_rolling_2y']].plot()

#df['ret_log'].plot()
plt.show()
print(1)
