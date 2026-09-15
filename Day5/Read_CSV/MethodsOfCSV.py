import pandas as pd
data=pd.read_csv("student.csv")
print(data.info())
print(data.head())
print(data.head(3))
print(data.tail())
print(data.describe())
