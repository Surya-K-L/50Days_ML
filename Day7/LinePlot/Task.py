import matplotlib.pyplot as plt
subjects = ["Maths", "Python", "DBMS", "OS", "ML"]
marks = [78, 85, 80, 72, 90]
plt.plot(subjects,marks,marker="o")
plt.title("Student Marks")
plt.xlabel("Subject")
plt.ylabel("Mark")
plt.grid()
plt.show()