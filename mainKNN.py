from knn import knn


a = [[1, 149, 68, 29, 127, 29.3, 0.349, 42]]
model = knn('diabetes.csv')
output = model.predict(a)
print(output[0])


