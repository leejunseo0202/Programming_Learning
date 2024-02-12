import cv2
from chap04.Common.utils import put_string

def bright_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_BRIGHTNESS,value)

def contrast_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_CONTRAST, value)

capture = cv2.VideoCapture(0)
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH,400)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
capture.set(cv2.CAP_PROP_BRIGHTNESS,0)
capture.set(cv2.CAP_PROP_CONTRAST, 0)

title = "Change Camera Properties"
cv2.namedWindow(title)
cv2.createTrackbar('bright',title, 0, 255, bright_bar)
cv2.createTrackbar('contrast', title, 0, 100, contrast_bar)

while True:
    ret, frame=capture.read()
    if not ret:break
    if cv2.waitKey(30) >=0: break
    bright = int(cv2.getTrackbarPos('bright', title))
    contrast = int(cv2.getTrackbarPos('contrast', title))
    put_string(frame, 'bright : ', (10, 240), bright)
    put_string(frame, 'contrast : ', (10, 270), contrast)
    cv2.imshow(title, frame)

capture.release()