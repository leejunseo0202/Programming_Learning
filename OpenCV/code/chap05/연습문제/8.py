import numpy as np, cv2

image = cv2.imread("c:/computervision/chap05/image/img2.jpg", cv2.IMREAD_GRAYSCALE)
image=image[400:1200,400:1200]
if image is None: raise Exception("영상 입력 오류")

center = (190, 170)
size = (150, 200)
ellipse=np.full((500,500), 0, np.uint8)
cv2.ellipse(ellipse, center, size, 0, 0, 360, 255, -1)

(w,h)=ellipse.shape[:2]
roi=image[:w,:h]

background=cv2.bitwise_and(roi, roi, mask=ellipse)

cv2.imshow("image", background)
cv2.waitKey()