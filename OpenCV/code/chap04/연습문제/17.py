import numpy as np, cv2

capture = cv2.VideoCapture(0)
if capture.isOpened()==False: raise Exception("카메라 연결 안됨")

title = '1'
cv2.namedWindow(title)

while True:
    ret, frame=capture.read()
    if not ret:break
    if cv2.waitKey(30) >=0: break

    flip_img=cv2.flip(frame, 1)
    cv2.imshow(title, flip_img)

capture.release()