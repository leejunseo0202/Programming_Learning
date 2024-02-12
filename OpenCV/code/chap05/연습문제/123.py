import numpy as np, cv2

pts1 = np.array([(100, 50, 1), (400, 50, 1),
                 (400, 250, 1), (100, 250, 1)], np.float32)

theta = 45 * np.pi / 180
m = np.array([[np.cos(theta), -np.sin(theta), 0],
              [np.sin(theta),  np.cos(theta), 0],
              [0,              0,             1]], np.float32)

delta = (pts1[2] - pts1[0])//2
center = pts1[0] + delta

t1 = np.eye(3, dtype=np.float32)
t2 = np.eye(3, dtype=np.float32)

center=-center
a = cv2.gemm(t1, center, 1, None, 1, flags=cv2.GEMM_1_T)
print(a)

image = np.full((400, 500, 3), 255, np.uint8)
cv2.polylines(image, [np.int32(pts1[:, :2])], True, (0, 255, 0), 2)
cv2.polylines(image, [np.int32(a)], True, (0, 255, 0), 2)
cv2.imshow("image", image)
cv2.waitKey(0)