import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('01_iris.csv')

df.plot.scatter(x='SepalLengthCm',y='SepalWidthCm',marker='o',linestyle='-',color='b',label='Sepale')

plt.xlabel('Lungimea sepalei')
plt.ylabel('Latimea sepalei')
plt.title('Grafic linie- relatia dintre lungimea si latimea sepalei')
plt.legend()
plt.grid(True)
plt.show()
