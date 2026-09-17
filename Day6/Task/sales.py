import pandas as pd
data=pd.read_csv("sales_data.csv")

#find missing values
print(data.isnull())
print(data.isnull().sum())

#fill missing value with the median value
Price_Median_Value=data["Price"].median()
data["Price"]=data["Price"].fillna(Price_Median_Value)

print(data)

Quantity_Median_Value=data["Quantity"].median()
data["Quantity"]=data["Quantity"].fillna(Quantity_Median_Value)
print(Quantity_Median_Value)

#remove duplicates
print(data.duplicated().sum())
data=data.drop_duplicates()
print(data.duplicated().sum())


#check datatypes
print(data.dtypes)


#Outliers
Q1=data["Price"].quantile(0.25)
Q3=data["Price"].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
print("Lower",lower)
print("Upper",upper)

#Encoding
data=pd.get_dummies(data,columns=["Category"])
print(data)

#final check
print(data.isnull().sum())
print(data.isnull())
print(data)

data.to_csv("Cleaned_Sales_Data",index=False)
print("Data is cleaned successfully")