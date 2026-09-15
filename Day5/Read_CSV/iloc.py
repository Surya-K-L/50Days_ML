import pandas as pd
data=pd.read_csv("student.csv")
print(data.iloc[:3])

print(data.iloc[0:3,0:2])
