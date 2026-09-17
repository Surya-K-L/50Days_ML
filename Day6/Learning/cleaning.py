import pandas as pd
data=pd.read_csv("employee.csv")
print(data)


print(data.isnull())
print(data.isnull().sum())

#remove duplicates
data=data.drop_duplicates()
print(data)

#check datatypes
print(data.dtypes)

#data to numeric
data["Age"]=pd.to_numeric(data["Age"],errors="coerce")
print(data)

data["Age"]=data["Age"].fillna(data["Age"].median())
print("After filling missing age",data)

#checking duplicates
print("Duplicates Rows: ")
print(data[data.duplicated()])
print("Number of Duplicates:")
print(data.duplicated().sum())

#remove duplicates
data=data.drop_duplicates()
print("After removing duplicates:")
print(data)

#employee age less than 18
print(data[(data["Age"]<18)|(data["Age"]>60)])

#salary negative
print(data[data["Salary"]<0])
valid_salary=data.loc[data["Salary"]>=0,"Salary"].median()
data.loc[data["Salary"]<0,"Salary"]=valid_salary
print("After Fixing Salary:")
print(data)

#invalid age
print(data[(data["Age"]<18) | (data["Age"]>60)])
valid_age_median=data.loc[
    data["Age"].between(18,60),"Age"
].median()
data.loc[
    ~data["Age"].between(18,60),"Age"
]=valid_age_median
print("\nAfter Fixing Age: ")
print(data)



#Outliers
Q1= data["Salary"].quantile(0.25)
Q3=data["Salary"].quantile(0.75)
IQR=Q3-Q1
lower =Q1-1.5*IQR
upper =Q3+1.5*IQR
print("\nLower Bound: ",lower)
print("\nUpper Bound: ",upper)

#find the employees whose salary is outside the iqr boundaries
# outliers=data[(data["Salary"]<lower)|(data["Salary"]>upper)]

# print("\n Salary Outliers: ")
# print(outliers)

#Encoding
data=pd.get_dummies(data,columns=["Department"])
print(data)

print(data.isnull().sum())
print(data.duplicated().sum())
print(data.dtypes)
print(data)

data.to_csv("CleanedData.csv",index=False)
print("\nCleaned Dataset is stored successfully")
