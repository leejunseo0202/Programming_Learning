import numpy as np, cv2

image = cv2.imread("c:/computervision/chap06/image/img1.jpg", 1)
if image is None : raise Exception("영상파일 읽기 오류")

Y = np.zeros((image.shape[0],image.shape[1]), np.float32)
Cb = np.zeros((image.shape[0],image.shape[1]), np.float32)
Cr = np.zeros((image.shape[0],image.shape[1]), np.float32)

b, g, r = cv2.split(image)
Y = 0.299*r + 0.587*g + 0.114*b
Cb = (r-Y)*0.564 + 128
Cr = (b-Y)*0.713 + 128

Y = np.round(Y)
Y = Y.astype('uint8')
Cb = np.round(Cb)
Cb = Cb.astype('uint8')
Cr = np.round(Cr)
Cr = Cr.astype('uint8')

zero = np.zeros((image.shape[0],image.shape[1]), np.uint8)
YCbCr = cv2.merge([Y, Cr, Cb])
YCC = cv2.split(YCbCr)

cv2.imshow('YCbCr', YCbCr)
cv2.imshow('Y', YCC[0])
cv2.imshow('Cr', YCC[1])
cv2.imshow('Cb', YCC[2])
cv2.waitKey(0)