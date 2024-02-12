import numpy as np

np.random.seed(10)
a=np.random.randint(1,100, 500)

b=np.zeros((101), np.int64)

for i in a:
    b[i]+=1;

max=0
for i in b:
    if(max<b[i]):
        max=b[i]

print(max)