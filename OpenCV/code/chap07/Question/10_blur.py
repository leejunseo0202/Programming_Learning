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

image = cv2.imread("/chap07/image/1.jpg", cv2.IMREAD_COLOR)
if image is None : raise Exception("영상파일 읽기 오류")
data = [1/9, 1/9, 1/9,
        1/9, 1/9, 1/9,
        1/9, 1/9, 1/9]

b, g, r = cv2.split(image)
mask = np.array(data, np.float32).reshape(3, 3)

blur_b = filter(b, mask)
blur_b = blur_b.astype('uint8')
blur_g = filter(g, mask)
blur_g = blur_g.astype('uint8')
blur_r = filter(r, mask)
blur_r = blur_r.astype('uint8')

dst = cv2.merge((blur_b, blur_g, blur_r))

opencv = cv2.filter2D(image, -1, mask)
cv2.imshow("blur_user", dst)
cv2.imshow("orginal", image)
cv2.imshow("blur_opencv", opencv)
cv2.waitKey()