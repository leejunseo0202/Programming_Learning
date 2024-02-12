import numpy as np, cv2

image=cv2.imread('/chap07/image/1.jpg', cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("이미지읽기 오류")
cv2.namedWindow('dst')

def threshold(value):
    pass

cv2.createTrackbar('th1', 'dst', 0, 255, threshold)
cv2.createTrackbar('th2', 'dst', 0, 255, threshold)

while True:
    if cv2.waitKey(30) >= 0: break

    th1 = cv2.getTrackbarPos('th1', 'dst')
    th2 = cv2.getTrackbarPos('th2', 'dst')

    dst = cv2.Canny(image, th1, th2)
    cv2.imshow('dst', dst)
