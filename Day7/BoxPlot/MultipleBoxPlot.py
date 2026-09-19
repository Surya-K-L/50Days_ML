import matplotlib.pyplot as plt
IT = [45000, 50000, 55000, 60000, 65000]

HR = [40000, 45000, 48000, 52000, 55000]

Finance = [50000, 60000, 65000, 70000, 75000]

data=[IT,HR,Finance]
plt.boxplot(data)
plt.xticks(
    [1,2,3],
    ["IT","HR","Finance"]
)
plt.title("Salary Distribution by Department")
plt.ylabel("Salary")
plt.show()