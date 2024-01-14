from sklearn import datasets

iris = datasets.load_iris()

print(iris.keys())

nrows,ncols=iris.data.shape
print(f"Fisierul iris are {nrows} randuri si {ncols} coloane")
print(iris.feature_names)
print(iris.DESCR)