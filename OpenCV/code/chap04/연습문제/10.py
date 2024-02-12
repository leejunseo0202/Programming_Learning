import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 20, (255, 0, 0))
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img, (x, y, 30, 30), (0, 0, 255), 1)
    cv2.imshow(title, img)

img = np.zeros((1000,1000, 3), np.uint8)
img[:]=(255)

title='mouse event'
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()