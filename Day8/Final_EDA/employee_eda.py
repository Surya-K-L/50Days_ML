import pandas as pd
data=pd.read_csv("../Dataset/employee_eda.csv")
print(data)
print(data.shape)
print(data.columns)
print(data.dtypes)
print(data.isnull().sum())
print(data.describe())