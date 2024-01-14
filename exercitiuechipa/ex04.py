import pandas as pd


df = pd.read_csv('01_iris.csv')

specii=df.groupby('Species')
print(specii['SepalLengthCm'].mean())
print(specii['SepalWidthCm'].mean())
print(specii['PetalLengthCm'].mean())
print(specii['PetalWidthCm'].mean())

print(specii['SepalLengthCm'].std())
print(specii['SepalWidthCm'].std())
print(specii['PetalLengthCm'].std())
print(specii['PetalWidthCm'].std())

print(specii['SepalLengthCm'].quantile())
print(specii['SepalWidthCm'].quantile())
print(specii['PetalLengthCm'].quantile())
print(specii['PetalWidthCm'].quantile())