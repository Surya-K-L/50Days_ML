import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("../Dataset/employee_eda.csv")
sns.boxplot(x=data["Salary"])
plt.title("Salary Box Plot")
plt.xlabel("Salary")
plt.show()
