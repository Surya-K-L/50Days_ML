import matplotlib.pyplot as plt

days=[1,2,3,4,5,6,7]
temperature=[30,23,25,32,27,22,21]

plt.plot(days,temperature,marker="o")
plt.title("Weekly Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.grid()
plt.show()