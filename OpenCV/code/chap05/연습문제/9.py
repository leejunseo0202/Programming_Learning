import numpy as np,cv2

m=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
m=np.array(m, np.uint8).reshape(3, 6)

m_reduce1 = cv2.reduce(m, 0, cv2.REDUCE_AVG)
m_reduce2 = cv2.reduce(m, 1, cv2.REDUCE_AVG)

print("orginal=\n%s\n" %m)
print("reduce1=\n%s\n" %m_reduce1)
print("reduce2=\n%s\n" %m_reduce2)