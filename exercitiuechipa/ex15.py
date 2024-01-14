import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('01_iris.csv')

sns.jointplot(data=df, x='SepalLengthCm',y='SepalWidthCm', kind="hex")
plt.show()