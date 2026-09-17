import pandas as pd
data=pd.read_csv("Stud.csv")
data["Age"]=data["Age"].fillna(data["Age"].mean())
print(data["Age"])

data["Marks"]=data["Marks"].fillna(data["Marks"].mean())
print(data["Marks"])