import numpy as np

a=[0,1,2,3,4,5,6,7,8,9]
b=np.array(a)

sum=0
for i in a:
    sum+=a[i]

print(sum, " ", sum/10)