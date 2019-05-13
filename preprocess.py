import pandas as pd
import numpy as numpy

class Preprocess:
    def __init__(self, path_data):
        self.path = path_data
    def precess(self):
        df_data = pd.read_csv(self.path)
        length = df_data.shape[0]
        df_data = pd.read_csv(
            self.path,  usecols=['Pregnancies', 'Glucose',  'BloodPressure',  'SkinThickness',  'Insulin',   'BMI',  'DiabetesPedigreeFunction',  'Age',  'Outcome'],
            dtype={'Pregnancies':'float', 'Glucose':'float',  'BloodPressure':'float',  'SkinThickness':'float',  'Insulin':'float',   'BMI':'float',  'DiabetesPedigreeFunction':'float',  'Age':'float',  'Outcome':'int32'})
        for i in range(0, length):
            print(i)
            if(df_data.iloc[i, 1] >= 126.0  and df_data.iloc[i, 5] >= 25.0 and df_data.iloc[i, 7] > 45 and df_data.iloc[i, 8] ==1  ):
                df_data.iloc[i, 8] = 2
        print(df_data)
        df_data.to_csv('data_diabe.csv', sep=',', encoding='utf-8')
if __name__=="__main__":
    pre = Preprocess("diabe.csv")
    df_data = pre.precess()
