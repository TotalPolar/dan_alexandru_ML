import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random


data = {'Neighborhood': ['A', 'B', 'C', 'D', 'E'],
        'Price': [100, 120, 80, 150, 90],
        'Occupancy': [80, 60, 90, 50, 70],
        'Review_Score': [4.5, 4.2, 4.8, 3.9, 4.6]}

for _ in range(100):
    data['Price'].append(random.randint(70,250))
    data['Neighborhood'].append(random.choice(['A','B','C','D','E']))
    data['Occupancy'].append(random.randint(0,100))
    data['Review_Score'].append(round(random.uniform(0,5),1))

df=pd.DataFrame(data)
#Pret
plt.figure(figsize=(14,8))
sns.barplot(x='Neighborhood',y='Price',data=df)
plt.title('Medie Pret locuinta in functie de Cartier')
plt.xlabel('Cartier')
plt.ylabel('Pretul locuintei')
plt.show()

plt.figure(figsize=(14,8))
sns.violinplot(x='Neighborhood',y='Price',data=df,palette='tab10')
plt.title('Distributia Pretului locuintei in functie de Cartier')
plt.xlabel('Cartier')
plt.ylabel('Pret locuinta')
plt.show()
#Ocupare
plt.figure(figsize=(14,8))
sns.barplot(x='Neighborhood',y='Occupancy',data=df,color='maroon')
plt.title('Medie Ocupare locuinta in functie de Cartier')
plt.xlabel('Cartier')
plt.ylabel('Ocuparea locuintei')
plt.show()

plt.figure(figsize=(14,8))
sns.violinplot(x='Neighborhood',y='Price',data=df,palette='Dark2')
plt.title('Distributia Ocuparii locuintei in functie de Cartier')
plt.xlabel('Cartier')
plt.ylabel('Ocupare locuinta')
plt.show()
#Scor
plt.figure(figsize=(14,8))
sns.barplot(x='Neighborhood',y='Review_Score',data=df,color='green')
plt.title('Medie Scor locuinta in functie de Cartier')
plt.xlabel('Cartier')
plt.ylabel('Scorul locuintei')
plt.show()

plt.figure(figsize=(14,8))
sns.violinplot(x='Neighborhood',y='Review_Score',data=df,palette='muted')
plt.title('Distributia Scorului locuintei in functie de Cartier')
plt.xlabel('Cartier')
plt.ylabel('Scor locuinta')
plt.show()
#Interrelational
plt.figure(figsize=(10,6))
sns.scatterplot(x='Price',y='Occupancy',hue='Neighborhood',data=df,palette='Dark2')
plt.title('Relatie intre Pret si Ocuparea locuintelor')
plt.xlabel('Pretul locuintei')
plt.ylabel('Ocuparea locuintei')
plt.show()

plt.figure(figsize=(10,6))
sns.scatterplot(x='Review_Score',y='Price',hue='Neighborhood',data=df,palette='muted')
plt.title('Relatie intre Pret si Scorul locuintelor')
plt.xlabel('Scorul locuintei')
plt.ylabel('Pretul locuintei')
plt.show()

plt.figure(figsize=(10,6))
sns.scatterplot(x='Occupancy',y='Review_Score',hue='Neighborhood',data=df,palette='muted')
plt.title('Relatie intre Ocuparea si Scorul locuintelor')
plt.xlabel('Ocuparea locuintei')
plt.ylabel('Scorul locuintei')
plt.show()

sns.pairplot(df,hue='Neighborhood',palette='husl')
plt.suptitle('Pair plot airbnb',y=1.02)
plt.show()