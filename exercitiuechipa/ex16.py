import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('01_iris.csv')

sns.scatterplot(data=df, x='SepalLengthCm',y='SepalWidthCm',hue='Species')
sns.kdeplot(data=df,x='SepalLengthCm',y='SepalWidthCm',cmap="mako")
plt.show()