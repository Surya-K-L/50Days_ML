import pandas as pd
data=pd.read_csv("employees.csv")
print(data)

#All employee whose salary>60000
print(data[data["Salary"]>60000])

#find the employees who work in IT dept
print(data[data["Department"]=="IT"])


#Find employees who have more than 4 years of experience AND salary greater than ₹55,000.
print(data[(data["Experience"]>4) & (data["Salary"]>55000)])

#Find employees whose age is below 30 OR salary is greater than ₹80,000.
print(data[(data["Age"]<30) | (data["Salary"]>80000)])


#Find employees from the Finance department whose experience is greater than 8 years.
print(data[(data["Department"]=="Finance") & (data["Experience"]>8)])