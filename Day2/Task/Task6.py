"""
Print all student names
Print all marks
Find the highest mark
Find the student with the highest mark"""




students = {
    101: {"name": "Surya", "mark": 85},
    102: {"name": "Arun", "mark": 92},
    103: {"name": "Kumar", "mark": 78}
}

for i in students:
    print(students[i]["name"])
for i in students:
    print(students[i]["mark"])

max=-1
for i in students:
    t=students[i]["mark"]
    if(t>max):
        max=t
print(max)

stu=""
for i in students:
    if(max==students[i]["mark"]):
        print(students[i]["name"])
