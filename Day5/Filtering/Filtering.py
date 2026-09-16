import pandas as pd
data=pd.read_csv("Student.csv")
print(data[data["Marks"]>80])
print(data[data["Marks"]<70])
print(data[(data["Department"]=="CSE")&(data["Marks"]>80)])
print(data[(data["Marks"]>90) | (data["Attendance"]>80)])
