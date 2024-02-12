import numpy as np,cv2

img=np.zeros((200,300), np.uint8)
title1='win mode1'
title2='win mode2'

cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2)
cv2.moveWindow(title1, 0, 0)
cv2.moveWindow(title2, 300, 200)

cv2.imshow(title1, img)
cv2.imshow(title2, img)
cv2.waitKey(0)
cv2.destroyAllWindows()