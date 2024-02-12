import numpy as np, cv2

m1=np.array([1,2,3,1,2,3], np.int8)
m2=np.array([3,3,4,2,2,3], np.int8)

m3=cv2.add(m1,m2)
m4=cv2.subtract(m1,m2)

print("[m1]=%s"%m1)
print("[m2]=%s"%m2)
print("[m3]=%s"%m3.flatten())
print("[m4]=%s"%m4.flatten())