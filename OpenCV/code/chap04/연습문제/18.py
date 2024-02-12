import numpy as np, cv2

def draw_bar(img, pt, w, bars):
    pt = np.array(pt, np.int)
    for bar in bars:
        (x, y), h = pt, w*6
        cv2.rectangle(img, (x, y, w, h), (0,0,0), -1)
        if bar == 0:
            y =
            h =
            cv2.rectangle(img, (x, y, w, h), (255, 255, 255), -1)
        pt += (int(w*1.5), 0)


red, green, blue=(0,0,255),(0,255,0),(255,0,0)
img=np.zeros((400,600,3), np.uint8)
img[:]=(255,255,255)

cv2.namedWindow('1', cv2.WINDOW_AUTOSIZE)
cv2.ellipse(img, (300,200), (100, 100), 0, 180, 360, red, -1)
cv2.ellipse(img, (300,200), (100, 100), 0, 0, 180, blue, -1)
cv2.ellipse(img, (350,200), (50, 50), 0, 180, 360, blue, -1)
cv2.ellipse(img, (250,200), (50, 50), 0, 0, 180, red, -1)

draw_bar(img, (100, 155), 15, [3])

cv2.imshow('1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()