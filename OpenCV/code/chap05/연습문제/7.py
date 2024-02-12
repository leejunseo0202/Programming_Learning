import numpy as np, cv2

logo=cv2.imread("c:/computervision/chap05/image/img3.jpg", cv2.IMREAD_COLOR)
logo = logo[:600,:]
if logo is None: raise Exception("영상 입력 오류")

blue, green, red = cv2.split(logo)

zero=np.zeros(logo.shape[:2], np.uint8)
list=[blue, zero, zero]
blue_image=cv2.merge(list)
list=[zero, green, zero]
green_image=cv2.merge(list)
list=[zero, zero, red]
red_image=cv2.merge(list)

cv2.imshow('1', blue_image)
cv2.imshow('2', green_image)
cv2.imshow('3', red_image)
cv2.waitKey()