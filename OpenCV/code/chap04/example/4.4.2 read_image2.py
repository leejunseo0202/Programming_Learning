import cv2
from chap04.Common.utils2 import print_matInfo

title1='babo'
color2gray=cv2.imread("../image/img.png", cv2.IMREAD_GRAYSCALE)
color2color=cv2.imread("../image/img.png", cv2.IMREAD_COLOR)
if color2gray is None or color2color is None:
    raise Exception("영상퍼일 읽기 에러")

print_matInfo(title1, color2gray)
print_matInfo('1', color2color)
cv2.imshow(title1, color2gray)
cv2.imshow('1', color2color)
cv2.waitKey(0)