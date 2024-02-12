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

image = cv2.imread("/chap07/image/1.jpg", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상파일 읽기 오류")
data1 = [-1, 0, 1,
        -1, 0, 1,
        -1, 0, 1]
data2 = [-1, -1, -1,
        0, 0, 0,
        1, 1, 1]

mask1 = np.array(data1, np.float32).reshape(3, 3)
mask2 = np.array(data2, np.float32).reshape(3, 3)

dst1 = filter(image, mask1)
dst2 = filter(image, mask2)
dst1, dst2 = np.abs(dst1), np.abs(dst2)
dst = cv2.magnitude(dst1, dst2)

dst = np.clip(dst, 0, 255).astype('uint8')

cv2.imshow("image", image)
cv2.imshow("prewitt", dst)
cv2.waitKey()