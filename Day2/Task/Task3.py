"""Find Duplicates"""

li= [10, 20, 30, 20, 40, 10, 50, 30]

tem=[]
for i in li:
    if(i not in tem):
        tem.append(i)
    else:
        print(i,end=" ")
print(tem)