student={
    "name":"Ajay",
    "age":21,
    "mark":85
}
#to print key
for key in student:
    print(key,end=" ")
    

#to print values
for key in student:
    print(student[key],end=" ")

print()  

#for both 
for key,value in student.items():
    print(key,":",value)
