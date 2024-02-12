import numpy as np, cv2

def onChange1(value):
    global thick
    thick=value

def onChange2(value):
    global Radius
    Radius=value

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        cv2.circle(img, (x, y), Radius, (255, 0, 0), thick)
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("2")
        cv2.rectangle(img, (x, y, 30, 30), (0, 0, 255), 1)
    cv2.imshow(title, img)

img = np.zeros((1000,1000, 3), np.uint8)
img[:]=(255)
thick=1
Radius=20

title='mouse event'
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('thick', title, thick, 10, onChange1)
cv2.createTrackbar('Radius', title, Radius, 50, onChange2)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()