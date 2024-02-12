import numpy as np, cv2

image = cv2.imread("c:/computervision/chap06/image/img1.jpg", 0)
if image is None : raise Exception("영상파일 읽기 오류")

projection_h = np.zeros((image.shape[0], 256), np.uint8)
list_h = cv2.reduce(image, dim=1, rtype=cv2.REDUCE_AVG)
list_h = list_h.flatten()
print(list_h)
for i in range(image.shape[0]):
    cv2.line(projection_h, (0, i), (list_h[i], i), 255, 1)

projection_w = np.zeros((256, image.shape[1]), np.uint8)
list_w = cv2.reduce(image, dim=0, rtype=cv2.REDUCE_AVG)
list_w = list_w.flatten()
for i in range(image.shape[1]):
    cv2.line(projection_w, (i, 0), (i, list_w[i]), 255, 1)
cv2.flip(projection_w, 0, projection_w)

cv2.imshow('1', projection_h)
cv2.imshow('2', projection_w)
cv2.imshow('3', image)
cv2.waitKey()