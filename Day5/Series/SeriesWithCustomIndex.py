import pandas as pd
marks=pd.Series(
    [80,89,97],
    index=["Surya","Jeeva","Ramesh"]
)
print(marks)
print(marks["Surya"])