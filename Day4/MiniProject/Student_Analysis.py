import numpy as np
marks=np.array([
    [85, 90, 78],
    [72, 88, 91],
    [60, 75, 80],
    [95, 92, 89],
    [55, 68, 70]
])

print("\nStudent Performance Analyser")

print("\nMarks Dataset")
print(marks)

print("\nNumber of Students: ",marks.shape[0])
print("\nNumber of Subjects: ",marks.shape[1])

print("\nOverall Statistics")
print("\nMean: ",np.mean(marks))
print("\nMedian: ",np.median(marks))
print("\nStandard Deviation: ",np.std(marks))
print("\nMinimum: ",np.min(marks))
print("\nMaximum: ",np.max(marks))


#Student wise avg
student_avg=np.mean(marks,axis=1)
print("\nStudent average: ",student_avg)

#subject avg
subject_avg=np.mean(marks,axis=0)
print("\nSubject Average: ",subject_avg)

#students score above 80
print("\nStudents score above 100",marks[marks>80])

