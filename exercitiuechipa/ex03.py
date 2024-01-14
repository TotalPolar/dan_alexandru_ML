import pandas as pd


df = pd.read_csv('01_iris.csv')

dfna=df.isna()
print(dfna[(dfna.SepalLengthCm==True)|(dfna.SepalWidthCm==True)|(dfna.PetalWidthCm==True)|(dfna.PetalLengthCm==True)|(dfna.Species==True)|(dfna.Id==True)])