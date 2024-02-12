import numpy as np, cv2

c = 1
while True:
    key = cv2.waitKeyEx(30)
    if key == 0x280000:
        c-=1
    elif key == 0x260000:
        c+=1
    elif key == 0x1B:
        break

    fname = "C:/computervision/chap07/image/{0:01d}.jpg".format(c)
    image = cv2.imread( fname, cv2.IMREAD_COLOR)
    if image is None : print(str(c) + "번 영상이 없습니다."); continue

    mask = np.ones((5, 17), np.uint8)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (5,5))
    gray = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 5)

    th_img = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)[1]
    morph = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask, iterations=3)

    cv2.imshow('image', image)
    cv2.imshow('binary', th_img)
    cv2.imshow('opening', morph)