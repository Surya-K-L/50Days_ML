import matplotlib.pyplot as plt
departments = ["IT", "HR", "Finance", "CSE"]
employees = [40, 25, 30, 35]

plt.bar(departments,employees)
plt.title("Employees by Department")
plt.xlabel("department")
plt.ylabel("employee")
for i in range(len(employees)):
    plt.text(i,employees[i],employees[i])
plt.show()

plt.barh(departments,employees)
plt.show()