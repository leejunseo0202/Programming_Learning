import numpy as np, cv2

image = cv2.imread("c:/computervision/chap06/image/img1.jpg", 1)
if image is None : raise Exception("영상파일 읽기 오류")
HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([HSV], [0, 1], None, [180,256], [0, 180, 0, 256])
hist = hist.astype('uint8')
H, S, V = cv2.split(HSV)

hsv = np.zeros((180, 256, 3), np.uint8)
h, s = np.indices(hsv.shape[:2])
hsv[:,:,0] = h
hsv[:,:,1] = s
hsv[:,:,2] = 0
for y in range(HSV.
                       shape[0]):
    for x in range(HSV.shape[1]):
        hsv[H[y,x],S[y, x], 2]+=1
hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

print(hsv.shape[:2], hist.shape[:2])
dst = cv2.bitwise_and(hsv, hsv, None, mask=hist)
cv2.imshow('1', image)
cv2.imshow('2', dst)
cv2.waitKey(0)