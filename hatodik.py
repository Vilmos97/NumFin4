import numpy as np
import pandas as pd
df=pd.DataFrame(columns=['num','fib'])
#append, pd.concat, pd.merge, pd.join
row1={'num':1, 'fib':1}
row2={'num':2, 'fib':1}
new_df=pd.DataFrame([row1,row2])
df=pd.concat([df, new_df],axis=0,ignore_index=True)
#df=df.append({'num':1, 'fib':1},ignore_index=True) régi verzió
print(df.dtypes)
print(df)


df2=pd.DataFrame(range(1,21),columns=['n'])
df2['fib']=np.nan
print(df2)
df2.loc[df2['n']==1,'fib']=1
#df2.loc[df2['n'] in [1,2],'fib']=1

for ix,row in df2.iterrows():
    #if ix in [1,2]:
        #row['fib']=1
        #df2.loc[ix,'fib']=1
    n=row['n']
    if n in [1,2]:
        df2.loc[ix, 'fib'] = 1

    print(ix)
    print(row)
    print(row['n'])


