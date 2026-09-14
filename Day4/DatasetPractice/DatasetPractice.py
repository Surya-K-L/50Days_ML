import numpy as np
marks = np.array([
    [85, 90, 78],
    [72, 88, 91],
    [60, 75, 80],
    [95, 92, 89],
    [55, 68, 70]
])
print(marks)
print("Dimesions: ",marks.ndim)
print("Shape: ",marks.shape)
print("Total ELements: ",marks.size)
print("Mean: ",np.mean(marks))
print("Median: ",np.median(marks))
print("Standard Deviation: ",np.std(marks))
print("Minimum mark: ",np.min(marks))
print("Maximum mark: ",np.max(marks))