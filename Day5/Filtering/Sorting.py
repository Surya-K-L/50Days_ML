import pandas as pd
data=pd.read_csv("Student.csv")
print(data)
print(data.sort_values("Marks")) #ASCENDING SORT
print(data.sort_values("Marks",ascending=False))
print(data.sort_values("Marks",ascending=False).head(5))