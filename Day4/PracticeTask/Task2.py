import numpy as np
arr=np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print("\nDimesion: ",arr.ndim)
print("\nShape: ",arr.shape)
print("\nSize: ",arr.size)
print("\nPrint Element 50: ",arr[1][1])
print("\nFirst Row: ",arr[0])
print("\nLast Row: ",arr[-1])
print("\nFirst Column: ",arr[:,0])
