import pandas as pd


df=pd.read_csv('01_iris.csv')

df=df.iloc[:,1:]

print(df)