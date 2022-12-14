import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_risk_free_rate():
    df=pd.read_csv('DTB3.csv')
    df.index=pd.to_datetime(df['DATE'])
    df=df[['DTB3']]
    df.columns=['risk_free']
    msk=df['risk_free']!='.'
    df=df[msk]
    df=df.astype(float)
    df=df/252
    return df
df_risk_free=get_risk_free_rate()
df_join=df.join(df_risk_free)
print(df_risk_free)

filename = 'BRK-B (1).csv'
df = pd.read_csv(filename)
df['ret_log_daily'] = np.log(df['Adj Close']/df['Adj Close'].shift(1))

df.index = pd.to_datetime(df['Date'])
t_day_in_year = 252
df['ret_log_y']=df['ret_log_daily'] * t_day_in_year

vol_windows_in_y = [0.25, 1,3,10]
cols_vol, cols_ret, cols_beta=[],[],[]
for year in vol_windows_in_y:
    col_vol='vol_'+str(year) + 'y'
    col_ret = 'ret_' + str(year) + 'y'
    col_beta='beta' + str(year) + 'y'
    cols_vol.append(col_vol)
    cols_ret.append(col_ret)
    cols_beta.append(col_beta)
    df[col_vol] = np.sqrt(t_day_in_year) * df['ret_log_daily'].rolling(int(year * t_day_in_year)).std()
    df[col_ret] = np.sqrt(t_day_in_year) * df['ret_log_daily'].rolling(int(year * t_day_in_year)).mean()
    df[col_beta] = df[col_ret]/df[col_vol]
    #df['vol_rolling_'+str(year) + 'y'] = df['ret_log'].rolling(year * t_day_in_year).std()

#df['vol_rolling_1y']=df['ret_log'].rolling(252).std()
#df['vol_rolling_2y']=df['ret_log'].rolling(504).std()
#df['ret_log'].plot()
#df[['vol_rolling_1y', 'vol_rolling_2y']].plot()
#df['col_ret'].plot()
#df['ret_log'].plot()
plt.show()


