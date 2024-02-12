import numpy as np
import cv2

switch_case = {
    2424832:"왼쪽 화살표",
    2555904:"오른쪽 화살표"
}

def onChange(value):
    global image, title
    image[:] = value
    cv2.imshow(title, image)

brigthness=0
image = np.zeros((300, 500), np.uint8)
title = 'Trackbar Event'
cv2.imshow(title, image)
cv2.createTrackbar('brightness', title, image[0][0], 255, onChange)

while True:
    key = cv2.waitKeyEx(100)
    if key == 2424832:
        if(brigthness-1<0):
            print('brigthness can not be minus')
        else:
            brigthness=brigthness-1
            cv2.setTrackbarPos('brightness', title, brigthness)
    elif key == 2555904:
        if(brigthness+1>256):
            print("brightness can not be over 255")
        else:
            brigthness=brigthness+1
            cv2.setTrackbarPos('brightness', title, brigthness)

    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()