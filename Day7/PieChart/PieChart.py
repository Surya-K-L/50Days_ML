import matplotlib.pyplot as plt
departments = ["IT", "HR", "Finance", "CSE"]
employees = [40, 20, 25, 15]
plt.pie(employees,labels=departments)
plt.title("Employee Distribution")
plt.show()
