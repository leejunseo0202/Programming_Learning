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

def rotate(img, degree, pt):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree/180) * np.pi
    sin, cos = np.sin(radian), np.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            jj, ii = np.subtract((j ,i), pt)
            y = -jj * sin + ii * cos
            x =  jj * cos + ii * sin
            x, y = np.add((x, y), pt)
            if contain((y, x), img.shape):
                dst[i, j] = billinear_value(img, (x, y))
    return dst

image = cv2.imread("c:/computervision/chap08/image/1.jpg", cv2.IMREAD_COLOR)

pt = [100, 100]

b, g, r = cv2.split(image)
dst_b = rotate(b, 30, pt)
dst_g = rotate(g, 30, pt)
dst_r = rotate(r, 30, pt)

dst = cv2.merge((dst_b, dst_g, dst_r))

cv2.imshow("image", image)
cv2.imshow("dst", dst)
cv2.waitKey()