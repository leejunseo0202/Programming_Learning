import numpy as np, cv2

def mopholgy(image, mask=None):
    dst = np.zeros(image.shape, np.uint8)
    if mask is None : mask = np.ones((3, 3), np.uint8)

    rows, cols = image.shape[:2]
    mcnt = cv2.countNonZero(mask)
    for i in range(1, rows -1):
        for j in range(1, cols - 1):
            y1, y2 = i - 1, i + 2
            x1, x2 = j - 1, j + 2

            roi = image[y1:y2, x1:x2]
            temp = cv2.bitwise_and(roi, mask)
            cnt = cv2.countNonZero(temp)
            dst[i, j] = 255 if (cnt == mcnt) else 0

    for i in range(1, rows -1):
        for j in range(1, cols - 1):
            y1, y2 = i - 1, i + 2
            x1, x2 = j - 1, j + 2

            roi = image[y1:y2, x1:x2]
            temp = cv2.bitwise_and(roi, mask)
            cnt = cv2.countNonZero(temp)
            dst[i, j] = 0 if (cnt == 0) else 255
    return dst

def salt_pepper_noise(img, n):
    h, w = img.shape[:2]
    x, y = np.random.randint(0, w, n), np.random.randint(0, h, n)
    noise = img.copy()
    for(x, y) in zip(x,y):
        noise[y, x] = 0 if np.random.rand() < 0.5 else 255
    return noise

image = cv2.imread("c:/computervision/chap07/image/1.jpg", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상파일 읽기 오류")
noise = salt_pepper_noise(image, 10000)

data = [0, 1, 0,
        1, 1, 1,
        0, 1, 0]
mask = np.array(data, np.uint8).reshape(3, 3)
th_img = cv2.threshold(noise, 128, 255, cv2.THRESH_BINARY)[1]

dst = mopholgy(th_img, mask)

cv2.imshow('image', noise)
cv2.imshow('binary', th_img)
cv2.imshow('mopholgy', dst)
cv2.waitKey()
