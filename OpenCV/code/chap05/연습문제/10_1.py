import numpy as np, cv2

capture = cv2.VideoCapture(0)
if capture.isOpened()==False:
    raise Exception("카메라 연결 안됨")

while True:
    ret, flame = capture.read()
    if not ret:break
    if cv2.waitKey(30) >=0 : break

    mask = np.zeros(flame.shape[:2], np.uint8)
    mask[100:201, 200:401]=255
    mean = cv2.mean(flame, mask)
    cv2.rectangle(flame, (200,100),(400, 200), (255, 0 ,0 ), 5)
    print("mean=",mean)
    cv2.imshow('1', flame)

capture.release()