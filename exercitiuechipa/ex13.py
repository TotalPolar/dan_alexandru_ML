import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('01_iris.csv')

plt.scatter(x=df['SepalLengthCm'],y=df['SepalWidthCm'],marker='o',linestyle='-',color='b',label='Sepale')

plt.scatter(x=df['PetalLengthCm'],y=df['PetalWidthCm'],marker='o',linestyle='-',color='r',label='Petale')

plt.legend()
plt.grid(True)
plt.show()