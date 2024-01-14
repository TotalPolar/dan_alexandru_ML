from sklearn import preprocessing
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

label_encoder = preprocessing.LabelEncoder()
df = pd.read_csv('01_iris.csv')
df['Species']= label_encoder.fit_transform(df['Species'])

print(df)

X=df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y=df['Species']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

knn=KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train,y_train)

predictions=knn.predict(X_test)
accuracy=accuracy_score(y_test,predictions)

print(f"Precizia modelului:{accuracy*100}%")