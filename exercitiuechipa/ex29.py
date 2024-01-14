import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

df=pd.read_csv('01_iris.csv')

label_encoder = preprocessing.LabelEncoder()
df['Species']= label_encoder.fit_transform(df['Species'])
X=df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y=df['Species']

train_data,test_data,train_labels,test_labels=train_test_split(X,y,
                                                               test_size=0.2,random_state=42)

model=LogisticRegression()
model.fit(train_data,train_labels)



predictions=model.predict(test_data)

acuratetea=accuracy_score(test_labels,predictions)
conf_matrix=confusion_matrix(test_labels,predictions)
raport_clasificare=classification_report(test_labels,predictions)

print(f"Acuratetea: {acuratetea}")
print(f"Confusion matrix: \n{conf_matrix}")
print(f"Raport de clasificare: \n{raport_clasificare}")
