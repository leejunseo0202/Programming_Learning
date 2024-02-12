import numpy as np, cv2

image = cv2.imread("/chap07/image/1.jpg", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상파일 읽기 오류")

lap = cv2.Laplacian(image, cv2.CV_16S, 1)

gaus1 = cv2.GaussianBlur(image, (3, 3), 0)
gaus2 = cv2.GaussianBlur(image, (9, 9), 0)
DoG = gaus1 - gaus2

canny = cv2.Canny(image, 100, 150)

cv2.imshow("image", image)
cv2.imshow("Laplacian", lap.astype('uint8'))
cv2.imshow("DoG", DoG.astype('uint8'))
cv2.imshow("Canny", canny.astype('uint8'))

cv2.waitKey()