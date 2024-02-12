import numpy as np, cv2

data = [3, 6, 3, -5, 6, 1, 2, -3, 5]
m1 = np.array(data, np.float32).reshape(3,3)
m2 = np.array([2, 10, 28], np.float32)

ret, inv = cv2.invert(m1, cv2.DECOMP_LU)
if ret:
    _, ans = cv2.solve(m1, m2, cv2.DECOMP_LU)

    print("answer : ", ans.flatten())

else:
    print("오류")