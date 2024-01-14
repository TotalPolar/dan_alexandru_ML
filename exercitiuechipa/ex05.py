import pandas as pd


df=pd.read_csv('01_iris.csv')

print(df[df['Species']=="Iris-setosa"])
print(df[df['Species']=="Iris-versicolor"])
print(df[df['Species']=="Iris-virginica"])