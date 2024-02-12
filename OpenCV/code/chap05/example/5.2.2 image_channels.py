import cv2

image=cv2.imread("C:/computervision/chap05/image/img.jpg")
if image is None: raise Exception("영상 읽기 오류")
if image.ndim !=3: raise Exception("컬러 영상 아님")

bgr = cv2.split(image)

cv2.imshow("image",image)
cv2.imshow("Blue Channel", bgr[0])
cv2.imshow("Green Channel", bgr[1])
cv2.imshow("Red Channel", bgr[2])

cv2.waitKey(0)