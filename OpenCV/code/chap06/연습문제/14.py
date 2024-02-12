import numpy as np, cv2

image = cv2.imread("c:/computervision/chap06/image/img1.jpg", 1)
if image is None : raise Exception("영상파일 읽기 오류")

HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(HSV)

dst = np.zeros((180,256, 3), np.uint8)
dst_H, dst_S, dst_V = cv2.split(dst)

for y in range(HSV.shape[0]):
    for x in range(HSV.shape[1]):
        dst_V[H[y,x],S[y, x]]+=1

for y in range(180):
    for x in range(256):
        dst_H[y, x] = y
        dst_S[y, x] = x

dst = cv2.merge((dst_H, dst_S, dst_V))
dst = cv2.cvtColor(dst, cv2.COLOR_HSV2BGR)

cv2.imshow('1', dst)
cv2.waitKey(0)