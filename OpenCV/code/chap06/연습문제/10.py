import numpy as np, cv2

image1 = np.zeros((50, 512), np.float32)
image2 = np.zeros((50, 512), np.float32)
rows, cols = image1.shape[:2]

for i in range(rows):
    for j in range(cols):
        image1.itemset((i, j), 1-j/512)
        print(j/512,"\n")

cv2.imshow('image1', image1)
cv2.waitKey(0)