import numpy as np, cv2

img=cv2.imread("C:/computervision/chap04/image/img.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow('title',img)
img1=(cv2.IMWRITE_JPEG_QUALITY, 100)
img2=(cv2.IMWRITE_PNG_COMPRESSION, 9)

cv2.imwrite("C:/computervision/chap04/image/img1.jpg", img1)
cv2.imwrite("C:/computervision/chap04/image/img2.png", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()