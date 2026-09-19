import matplotlib.pyplot as plt
salary = [
    30000, 32000, 35000, 36000, 38000,
    40000, 42000, 45000, 48000, 50000,
    52000, 55000, 58000, 60000, 150000
]

plt.boxplot(salary)
plt.title("Salary Distribution")
plt.ylabel("Salary")
plt.show()
