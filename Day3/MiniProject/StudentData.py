print("Student mark Files")
print("How many student details are you going")
stud=int(input())
for i in range(stud):
    file=open("StudentMarks.txt","a")
    print("Enter Stud Name: ")
    name=input()
    print("Enter the number of subjects")
    no_of_subj=int(input())
    total_no_of_sub=no_of_subj
    mark_lis=[]
    pass_fail="fail"
    while(no_of_subj>0):
        print("Enter the subject: ")
        subject=input()
        print("Enter the mark: ")
        mark=int(input())
        while(mark<0 or mark>100):
            print("Invalid mark")
            print("Please enter a valid mark")
            print("Enter the mark")
            mark=int(input())
        mark_lis.append(mark)
        if(mark>=40 and mark<=100):
            pass_fail="pass"
        no_of_subj-=1  
        file.write("name: "+name+"\n")
        file.write("subject:"+subject+"\n")
        file.write("mark:"+str(mark)+"\n")
        file.write("Pass/Fail: "+pass_fail+"\n")
        total=0
        for i in mark_lis:
            total+=i
        avg=total/total_no_of_sub
        file.write("average: "+str(avg)+"\n")

