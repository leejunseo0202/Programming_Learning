import numpy as np, cv2, math

def draw_point(x, y):
    pts.append([x, y])

def onMouse(event, x, y, flags, param):
    global pts, angle
    if (event == cv2.EVENT_LBUTTONDOWN and len(pts) == 0): draw_point(x, y)
    if (event == cv2.EVENT_LBUTTONUP and len(pts) == 1): draw_point(x, y)

    if len(pts) == 2:
        x1, y1, x2, y2 = pts[0][0], pts[0][1], pts[1][0], pts[1][1]
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)

        radian = math.atan(dx / dy)
        angle = 180 / np.pi * radian
        pts.append([1, 1])

    if len(pts) == 3:
        pt, scale = (0, 0), 1
        size = image.shape[::-1]

        rot_mat = cv2.getRotationMatrix2D(pt, angle, scale)
        dst = cv2.warpAffine(image, rot_mat, size, cv2.INTER_LINEAR)
        pts.append([1, 1])

        cv2.imshow('dst', dst)
        cv2.waitKey()

image = cv2.imread("c:/computervision/chap08/image/1.jpg", cv2.IMREAD_GRAYSCALE)

pts = []
cv2.imshow('image', image)
cv2.setMouseCallback('image', onMouse, 0)
cv2.waitKey()