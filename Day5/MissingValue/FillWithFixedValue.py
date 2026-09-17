import pandas as pd
data=pd.read_csv("Stud.csv")
data["Department"]=data["Department"].fillna("Unknown")
print(data["Department"])