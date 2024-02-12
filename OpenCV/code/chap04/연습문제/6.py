import numpy as np, cv2

img=np.zeros((300,400), np.uint8)
img.fill(100)

cv2.imshow('title', img)
cv2.resizeWindow('title', 500, 600)
cv2.waitKey(0)
cv2.destroyAllWindows()