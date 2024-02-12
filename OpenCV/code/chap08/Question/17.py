import numpy as np, cv2

image = cv2.imread("c:/computervision/chap08/image/1.jpg", cv2.IMREAD_GRAYSCALE)

h, w = image.shape

flip1 = np.array([[-1, 0, w], [0, 1, 0]], np.float32)
flip2 = np.array([[1, 0, 0],  [0, -1, h]], np.float32)
flip3 = np.array([[-1, 0, w], [0, -1, h]], np.float32)


dst1 = cv2.warpAffine(image, flip1, (w, h))
dst2 = cv2.warpAffine(image, flip2, (w, h))
dst3 = cv2.warpAffine(image, flip3, (w, h))
cv2.imshow("image", image)
cv2.imshow("1", dst1)
cv2.imshow("2", dst2)
cv2.imshow("3", dst3)
cv2.waitKey()