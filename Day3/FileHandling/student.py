file=open("student.txt","w")
file.write("Name: Surya\n")
file.write("Marks: 90\n")
file.close()


file=open("student.txt","r")
data=file.read()
print(data)

