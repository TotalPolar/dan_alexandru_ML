import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('01_iris.csv')
df=df.iloc[:,1:5]

sns.heatmap(data=df)
plt.show()