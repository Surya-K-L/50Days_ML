import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Sleep_Hours": [5, 6, 7, 6, 8, 7, 8, 9],
    "Marks": [35, 40, 50, 55, 65, 75, 85, 95]
}
df=pd.DataFrame(data)
print(df)
sns.pairplot(df)
plt.show()