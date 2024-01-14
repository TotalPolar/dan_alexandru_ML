from sklearn import preprocessing
import pandas as pd
from sklearn.model_selection import train_test_split


label_encoder = preprocessing.LabelEncoder()
df = pd.read_csv('01_iris.csv')
df['Species']= label_encoder.fit_transform(df['Species'])

print(df)

X=df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y=df['Species']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

print(X_train)
print(y_train)
print(X_test)
print(y_test)