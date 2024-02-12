import numpy as np, cv2

image1 = cv2.imread("c:/computervision/chap05/image/img2.jpg", cv2.IMREAD_GRAYSCALE)
image1 = image1[300:1000, 300:1000]
image2 = cv2.imread("c:/computervision/chap05/image/img.jpg", cv2.IMREAD_GRAYSCALE)
image2 = image2[:700, :700]
if image1 is None or image2 is None : raise Exception("이미지 읽기 오류")

dif_img1=cv2.subtract(image1, image2)
dif_img2=cv2.subtract(np.int16(image1), np.int16(image2))
abs_dif1=np.absolute(dif_img2).astype("uint8")
abs_dif2=cv2.absdiff(image1, image2)

titles = ['image1', 'image2', 'dif_img1', 'dif_img2', 'abs_dif1', 'abs_dif2']
for title in titles:
    cv2.imshow(title, eval(title))
cv2.waitKey(0)