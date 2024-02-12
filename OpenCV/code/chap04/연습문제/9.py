import numpy as np, cv2

img = np.zeros((600, 400, 3), np.uint8)

title='rectangle'
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
cv2.rectangle(img, (100, 100, 200, 300), (0, 0, 255))

cv2.imshow(title, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
