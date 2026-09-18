import matplotlib.pyplot as plt
marks = [45, 50, 52, 55, 58, 60, 62, 65, 67, 70,
         72, 74, 75, 78, 80, 82, 85, 88, 90, 95]
plt.hist(marks,bins=5)
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()