import pandas as pd
data={
    "Name":["Arun","Deepak","Kamalesh","Nithin","Suraj"],
    "Age":[23,24,22,21,20],
    "Department":["CSE","ML","DS","CSE","ML"],
    "Section":["A","B","C","A","B"]
}
df=pd.DataFrame(data)
print(df)