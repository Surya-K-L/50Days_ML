import pandas as pd
data=pd.read_csv("Student.csv")
print(data.groupby("Department")["Marks"].mean())
