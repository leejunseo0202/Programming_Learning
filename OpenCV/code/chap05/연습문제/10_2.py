import numpy as np, cv2

capture = cv2.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

while True:
    ret, flame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    b_sum, g_sum, r_sum = 0, 0, 0
    for x in range(200, 401):
        for y in range(100, 201):
            b, g, r = cv2.split(flame)
            b_sum += b[y, x]
            g_sum += g[y, x]
            r_sum += r[y, x]
    mean = [b_sum/20000, g_sum/20000, r_sum/20000]

    cv2.rectangle(flame, (200, 100), (400, 200), (255, 0, 0), 5)
    print("mean=", mean)
    cv2.imshow('1', flame)

capture.release()