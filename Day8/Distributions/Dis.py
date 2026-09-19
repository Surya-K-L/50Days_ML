import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("../Dataset/employee_eda.csv")
sns.histplot(data["Salary"],kde=True)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.show()