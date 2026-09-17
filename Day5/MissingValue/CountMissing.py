import pandas as pd
data=pd.read_csv("Stud.csv")
print(data.isnull().sum())

#Remove missing row
data=data.dropna()
print(data)