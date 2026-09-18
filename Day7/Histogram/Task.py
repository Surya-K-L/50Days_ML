import matplotlib.pyplot as plt
ages = [21, 22, 22, 23, 24, 24, 25, 25, 25, 26,
        27, 27, 28, 29, 30, 30, 31, 32, 35, 40]
plt.hist(ages, bins=5)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of People")
plt.show()