import matplotlib.pyplot as plt
subjects = ["Maths", "Python", "DBMS", "OS", "ML"]
marks = [78, 85, 80, 72, 90]
plt.bar(subjects,marks)
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
for i in range(len(marks)):
    plt.text(i,marks[i],marks[i])
plt.show()
