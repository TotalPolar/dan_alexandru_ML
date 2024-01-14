import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df = pd.read_csv('01_iris.csv')

print(df)

X=df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y=df['Species']

scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)
def knn(k):
    X_train,X_test,y_train,y_test=train_test_split(X_scaled,y,test_size=0.2,random_state=42)

    knn=KNeighborsClassifier(n_neighbors=k)

    knn.fit(X_train,y_train)

    predictions=knn.predict(X_test)
    accuracy=accuracy_score(y_test,predictions)

    print(f"Precizia modelului:{accuracy*100}%")
    print(f"Raportul detaliat al clasificarii: \n {classification_report(y_test,predictions,zero_division=1)}")
    return accuracy

acurateti=[]
for i in range(1,101):
    acurateti.append(knn(i))

array1=np.array(acurateti)
array1=array1.transpose()

array2= list(range(1,101))
array2=np.array(array2)
array3=np.c_[ array1, array2 ]

df1 = pd.DataFrame(array3, columns=['acuratete', 'k'])

df1.plot(x='k',y='acuratete',marker='o',linestyle='-',color='b',label='Vanzari')

plt.ylabel('Valoare K')
plt.xlabel('Acuratete algoritm')
plt.title('Grafic linie- acuratetea algoritmului KNN in functie de K')
plt.legend()
plt.grid(True)
plt.show()