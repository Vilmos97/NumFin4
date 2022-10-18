import pandas as pd

df_prop=pd.read_csv('property data.csv')
#print(df_prop)

df_prop['PID'].apply(lambda col:str(col)[:9])

df=pd.read_excel('stock_test.xlsx')
#print(df)
df_pivot=pd.pivot_table(df,index=['Date'],columns=['Stock'], values=['Price'])
#print(df_pivot)
#print(df.groupby('Stock').mean())
df['Stock_name']=df['Stock'].apply(lambda col: col[:-6])
print(df)
