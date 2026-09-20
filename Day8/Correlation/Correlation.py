import pandas as pd

data = pd.read_csv("../Dataset/employee_eda.csv")

print(data.corr(numeric_only=True))