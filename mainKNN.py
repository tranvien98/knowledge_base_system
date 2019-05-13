from knn import knn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
df_data = pd.read_csv("data_diabe.csv",  usecols=['Pregnancies', 'Glucose',  'BloodPressure',  'SkinThickness',
                                               'Insulin',   'BMI',  'DiabetesPedigreeFunction',  'Age'],
                           dtype={'Pregnancies': 'float', 'Glucose': 'float',  'BloodPressure': 'float',
                                  'SkinThickness': 'float',  'Insulin': 'float',   'BMI': 'float',
                                  'DiabetesPedigreeFunction': 'float',  'Age': 'float'})
print(df_data)
a = [[2.0, 138.0, 62.0, 35.0, 0.0, 33.6, 0.127, 47.0]]
model = knn('data_diabetes.csv')
output = model.predict(df_data)
print(output)


