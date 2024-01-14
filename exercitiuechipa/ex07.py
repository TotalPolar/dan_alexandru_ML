import pandas as pd


df=pd.read_csv('01_iris.csv')

print(df[0:4]['SepalLengthCm'])
print(df[0:4]['SepalWidthCm'])
print(df[0:4]['PetalLengthCm'])
print(df[0:4]['PetalLengthCm'])
print(df[0:4]['Species'])