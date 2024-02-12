import numpy as np, cv2

image = cv2.imread("/chap07/image/1.jpg", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("이미지 읽기 오류")

kernel = np.ones((5,5), np.float32)/25
convolution = cv2.filter2D(image, -1, kernel)

averaging = cv2.blur(image, (5,5))

gaussian = cv2.GaussianBlur(image, (5,5), 0)

median = cv2.medianBlur(image, 5)

bilateral = cv2.bilateralFilter(image, 9, 75, 75)

cv2.imshow("convolution", convolution)
cv2.imshow("averaging", averaging)
cv2.imshow("gaussian", gaussian)
cv2.imshow("median", median)
cv2.imshow("bilateral", bilateral)

cv2.waitKey()

#https://webnautes.tistory.com/1255