import numpy as np, cv2

def filter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)

    for i in range(1, rows -1):
        for j in range(1, cols - 1):
            y1, y2 = i - 1, i + 2
            x1, x2 = j - 1, j + 2
            roi = image[y1:y2, x1:x2].astype('float32')
            tmp = cv2.multiply(roi, mask)
            dst[i, j] = cv2.sumElems(tmp)[0]
    return dst

def filter2(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)

    for i in range(1, rows -1):
        for j in range(1, cols - 1):
            sum = 0.0
            for u in range(mask.shape[1]):
                for v in range(mask.shape[1]):
                    y, x = i + u - 1, j + v - 1
                    sum +=image[y, x]*mask[u, v]
            dst[i, j] = sum
    return dst


image = cv2.imread("/chap07/image/1.jpg", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상파일 읽기 오류")

data = [1/9, 1/9, 1/9,
        1/9, 1/9, 1/9,
        1/9, 1/9, 1/9]

mask = np.array(data, np.float32).reshape(3, 3)
blur1 = filter(image, mask)
blur1 = blur1.astype('uint8')
blur2 = filter2(image, mask)
blur2 = cv2.convertScaleAbs(blur2)

cv2.imshow("1", blur1)
cv2.imshow("2", blur2)
cv2.imshow("3", image)
cv2.waitKey()