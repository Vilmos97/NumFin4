import pandas as pd
import numpy as np
df_tlt = pd.read_csv('TLT.csv')
df_voo = pd.read_csv('VOO.csv')

df_test = pd.read_excel('test.xlsx', sheet_name='Munka1')
#print(df_tlt, df_voo, df_test)
df_test.to_csv('df_test_output.csv')

df = pd.DataFrame(data={'A': [3, 4, 'a'],
                        'B': ['dafd', 3, 5]})
#print(df)
#print(df_voo.head(10))
#print(df_voo.tail(10))
#print(df_voo.columns)
#print(df_voo.index)
#print(df_voo.dtypes)

#print(df['A'])
#df['C'] = ''
#del df['C']
#print(df)
#print(df_voo.loc[0, ])
#print(df_voo.loc[0, 'Adj Close'])
#print(df_voo.iloc[-1])
#print(df_voo.iloc[-1]['Adj Close'])
#print(df_voo.loc[0:5, 'Adj Close'])
df_voo_copy = df_voo.copy()
df_voo_copy.index = df_voo_copy['Date']
#print(df_voo_copy)
#print(df_voo_copy.iloc[0])
df_voo['Volume in thousands'] = df_voo['Volume'] / 1000
df_voo['Open Close Difference'] = df_voo['Open'] - df_voo['Close']
#print(df_voo)
df_merged = df_voo.merge(df_tlt, how='inner', on='Date', suffixes=('_voo','_tlt'))
#print(df_merged)
df_merged_filtered = df_merged[['Date','Adj Close_voo', 'Adj Close_tlt']]
#print(df_merged_filtered)

df_prop = pd.read_csv('property data.csv')
#print(df_prop.shape)
#print(df_prop.loc[df_prop['ST_NAME'] == 'BERKELEY',"NUM_BATH"])
#msk = df_prop['ST_NAME'].isin(["BERKELEY", "LEXINGTON"])
#print(df_prop.loc[msk, ])
#msk=(df_prop["ST_NUM"]<200) & (df_prop["ST_NAME"]=="LEXINGTON")
#print(df_prop.loc[msk])
#msk=df_prop["ST_NUM"].notnull()
#print(df_prop.loc[msk])
df_prop["PID"] = df_prop["PID"].fillna("UNKNOWN")
#print(df_prop)
df_prop_copy = df_prop.copy()
#for column in df_prop.copy.columns:
   # df_prop_copy[column] = df_prop_copy[column].fillna("UNKNOWN")

df_prop_copy_2=df_prop.copy()
df_prop_copy_2=df_prop_copy_2.fillna("UNKNOWN")
#print(df_prop_copy_2)

#print(df_voo)
df_voo['effective_return']=(df_voo['Adj Close']/df_voo['Adj Close'].shift(1))-1

df_voo['log_return']=np.log(df_voo['Adj Close']/df_voo['Adj Close'].shift(1))

df_voo['cumsum_log_return'] = df_voo['log_return'].cumsum()
print(df_voo)
