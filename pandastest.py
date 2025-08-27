import numpy as np
import pandas as pd
s=pd.Series([10,20,30,40])
print(s)
data={'Name':['Nelvin','Bob','Diya','John','Maya'],'Age':[20,30,np.nan,33,44],'City':['Mumbai','Chennai','Pune','Kochi',None]}
df=pd.DataFrame(data)
print(df)
print(df.head())
print(df.head(3))
print(df.tail())
print(df.tail(4))
print(df.info())
print(df.describe())
print(df.columns)
print(df.shape)
df=pd.DataFrame(data,index=['a','b','c','d','e'])
print(df.loc['a'])
print(df.loc['b','Name'])
print(df.loc[:,['Name','City']])
print(df.iloc[0])
print(df.iloc[1,0])
print(df.iloc[:,0:2])
print(df.isnull())
print(df.dropna())
print(df.fillna(0))
df['Age'].fillna(df['Age'].mean(),inplace=True)
print(df)



