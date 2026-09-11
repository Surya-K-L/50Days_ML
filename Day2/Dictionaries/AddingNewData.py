student={
    "name":"Ajay",
    "age":21,
    "mark":85
}
student["department"]="CSE"
print(student)


student["mark"]=90
print(student)

#remove data
student.pop("mark")
print(student)