import numpy as np
data=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
print(np.mean(data))
print(np.mean(data,axis=1)) #1 each row , 0 each column
print(np.mean(data ,axis=0))