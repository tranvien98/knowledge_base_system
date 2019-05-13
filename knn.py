from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
class knn:
    def __init__(self, path_csv):
        print('train knn ...')
        self.df_data = pd.read_csv(path_csv,  usecols=['Pregnancies', 'Glucose',  'BloodPressure',  'SkinThickness',
                                 'Insulin',   'BMI',  'DiabetesPedigreeFunction',  'Age',  'Outcome'],
            dtype={'Pregnancies': 'float', 'Glucose': 'float',  'BloodPressure': 'float',
              'SkinThickness': 'float',  'Insulin': 'float',   'BMI': 'float',
                'DiabetesPedigreeFunction': 'float',  'Age': 'float',  'Outcome': 'int32'})
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(
            self.df_data.loc[:, self.df_data.columns != 'Outcome'], self.df_data['Outcome'], stratify=self.df_data['Outcome'], test_size=0.25)
    def predict(self, inputt):
        k_nn = KNeighborsClassifier(n_neighbors=13, weights='distance')
        k_nn.fit(self.X_train, self.Y_train)
        output = k_nn.predict(inputt)
        print(accuracy_score(k_nn.predict(self.X_test), self.Y_test))
        return output
