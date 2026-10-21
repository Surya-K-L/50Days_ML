import numpy as np
lis=[10,20,30,40,50]
mea=np.mean(lis)
st=np.std(lis)
x=50
z_score=(x-mea)/st
print(z_score)