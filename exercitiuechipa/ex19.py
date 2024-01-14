import pandas as pd

df = pd.read_csv('01_iris.csv')

print(df)

X=df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y=df['Species']