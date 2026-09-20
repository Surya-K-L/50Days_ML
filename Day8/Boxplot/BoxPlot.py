import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("../Dataset/employee_eda.csv")
sns.boxplot(
    x="Department",
    y="Salary",
    data=data
)
plt.title("Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()