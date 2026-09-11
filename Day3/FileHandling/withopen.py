with open("student.txt","a") as file:
    file.write("Name: Jeeva\n")
    file.write("Marks: 85")

with open("student.txt","r") as file:
    data=file.read()
print(data)