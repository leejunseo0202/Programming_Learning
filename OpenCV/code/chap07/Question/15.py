import numpy as np, cv2

def median_filter(image, size):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)

    for i in range(1, rows -1):
        for j in range(1, cols - 1):
            y1, y2 = i - 1, i + 2
            x1, x2 = j - 1, j + 2
            mask = image[y1:y2, x1:x2].flatten()

            sort_mask = cv2.sort(mask, cv2.SORT_EVERY_COLUMN)
            dst[i, j] = sort_mask[sort_mask.size//2]

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

noise = salt_pepper_noise(image, 500)
med_img = median_filter(noise, 5)

cv2.imshow("image", image)
cv2.imshow("noise", noise)
cv2.imshow("median", med_img)
cv2.waitKey()