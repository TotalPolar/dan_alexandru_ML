import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('01_iris.csv')

df.plot.scatter(x='PetalLengthCm',y='PetalWidthCm',marker='o',linestyle='-',color='b',label='Petale')

plt.xlabel('Lungimea petalei')
plt.ylabel('Latimea petalei')
plt.title('Grafic linie- relatia dintre lungimea si latimea petalei')
plt.legend()
plt.grid(True)
plt.show()
