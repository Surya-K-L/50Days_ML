"""Word Frequency
    Output:
    python : 3
    java : 2
    c : 1
"""

li=["python","java","python","c","python" ,"java"]
tem=[]
c=0
for i in li:
    if(i not in tem):
        tem.append(i)
        t=li.count(i)
        print(i,":",t)
    
    