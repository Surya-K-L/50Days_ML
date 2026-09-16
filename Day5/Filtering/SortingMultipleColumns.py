import pandas as pd
data=pd.read_csv("Student.csv")
print(data.sort_values(
    ["Department","Marks"],
    ascending=[True,False]
))