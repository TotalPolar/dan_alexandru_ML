import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('01_iris.csv')

nrspecii = df['Species'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(nrspecii, colors=['red', 'blue', 'green'])
plt.title('Frecvența Speciilor in Iris')
plt.show()
