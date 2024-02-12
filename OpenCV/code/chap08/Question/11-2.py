import numpy as np, cv2

def contain(p, shape):
    return 0<=p[0] < shape[0] and 0<=p[1]<shape[1]

def billinear_value(img, pt):
    x, y = np.int32(pt)
    if x>= img.shape[1]-1:x=x-1
    if y>= img.shape[0]-1:y=y-1

    P1, P2, P3, P4 = np.float32(img[y:y+2, x:x+2].flatten())

    alpha, beta = pt[1] - y, pt[0] - x
    M1 = P1 + alpha * (P3 - P1)
    M2 = P2 + alpha * (P4 - P2)
    P = M1 + beta * (M2 - M1)
    return np.clip(P, 0, 255)

image = cv2.imread("c:/computervision/chap08/image/1.jpg", cv2.IMREAD_GRAYSCALE)
image = image[100:400, 100:400]

pt, angle, scale = (100, 100), 30, 1
size = image.shape[::-1]

pt1 = np.array([(20, 70), (20, 240), (300, 110)], np.float32)
pt2 = np.array([(120, 20), (10, 180), (280, 260)], np.float32)
aff_mat = cv2.getAffineTransform(pt1, pt2)

dst = cv2.warpAffine(image, aff_mat, size, cv2.INTER_LINEAR)
cv2.imshow('image', image)
cv2.imshow('dst', dst)
cv2.waitKey()

