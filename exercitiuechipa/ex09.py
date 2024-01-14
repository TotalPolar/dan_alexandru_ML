import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('01_iris.csv')

df['Species'].hist(bins=5,color='skyblue',edgecolor='black')
plt.xlabel('Specie')
plt.ylabel('Frecventa')
plt.title('Histograma-distributia speciilor')
plt.show()