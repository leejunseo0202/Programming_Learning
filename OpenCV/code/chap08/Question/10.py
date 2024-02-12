import numpy as np, cv2

def contain(p, shape):
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]

def translate(img, pt):
    dst = np.zeros(img.shape, img.dtype)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            x, y = np.subtract((j, i), pt)
            if contain((y, x), img.shape):
                dst[i, j] = img[y, x]
    return dst

image = cv2.imread("c:/computervision/chap08/image/1.jpg")

dst1 = translate(image, (50, 60))

M = np.float64([[1, 0, 50], [0, 1, 60]])
dst2 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow('1', dst1)
cv2.imshow('2', dst2)
cv2.waitKey()