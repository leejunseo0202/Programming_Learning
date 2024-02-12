import numpy as np, cv2

capture = cv2.VideoCapture(0)
if capture.isOpened()==False: raise Exception("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)

title = '1'
cv2.namedWindow(title)

while True:
    ret, frame=capture.read()
    if not ret:break
    if cv2.waitKey(30) >=0: break

    cv2.rectangle(frame, (200, 100), (300,300),(0, 0, 255), 3, cv2.LINE_4)
    b, g, r = cv2.split(frame)
    g[100:300,200:300]+=50
    cv2.merge((b,g,r),frame)
    cv2.imshow(title, frame)

capture.release()
