import numpy as np, cv2

video = cv2.VideoCapture("c:/computervision/chap05/image/mv.mp4")
if video.isOpened() == False:raise Exception("동영상 연결 안됨")

while video.isOpened():
    ret, flame = video.read()
    if not ret : break
    if cv2.waitKey(30)>=0 : break

    flame1 = flame[:800, 300:1000]
    flame1[100:200, 100:200] += 50

    mask = np.zeros(flame1.shape[:2], np.uint8)
    mask[500:600, 500:600] = 255
    flame2 = cv2.convertScaleAbs(flame1, alpha=3, beta=1)

    flame2 = cv2.copyTo(flame2, mask, flame1)
    cv2.imshow('1', flame2)

cv2.waitKey(0)
video.release()