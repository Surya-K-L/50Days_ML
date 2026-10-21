import pandas as pd
marks = pd.Series([45, 48, 50, 51, 53, 55, 200])
q1=marks.quantile(0.25)
q3=marks.quantile(0.75)
IQR=q3-q1
lower=q1-1.5*IQR
upper=q3+1.5*IQR
outliers=marks[(marks<lower)|(marks>upper)]
print(q1)
print(q3)
print(IQR)