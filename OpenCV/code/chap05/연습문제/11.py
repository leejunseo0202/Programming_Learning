##https://webnautes.tistory.com/1250
import numpy as np ,cv2

capture=cv2.VideoCapture(0)
if capture.isOpened() == False:raise Exception("카메라 연결 안됨")

while True:
    ret, flame = capture.read()
    if not ret:break
    if cv2.waitKey(30)>=0 : break

    cv2.rectangle(flame, (30, 30), (350, 270), (255, 0, 0), 5)
    flame = flame[30:271, 30:351]

    M = np.float32([[1, 0, 30], [0, 1, 30]])
    main = cv2.warpAffine(flame, M, (400, 300))
    cv2.imshow('main_window', main)

capture.release()
cv2.destroyAllWindows()