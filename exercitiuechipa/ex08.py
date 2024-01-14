import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('01_iris.csv')

sns.pairplot(df,hue='Species',palette='husl')
plt.suptitle('Pair plot pentru caracteristic iris',y=1.02)
plt.show()