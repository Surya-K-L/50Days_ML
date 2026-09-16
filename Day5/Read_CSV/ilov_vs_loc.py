import pandas as pd
data=pd.read_csv("student.csv")
print(data.iloc[2])
print(data.loc[2])