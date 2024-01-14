import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('01_iris.csv')
sns.scatterplot(data=df,x='PetalLengthCm',y='PetalWidthCm',hue='Species')
plt.show()