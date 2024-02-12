import numpy as np, cv2

img1=cv2.imread('C:/computervision/chap06/image/img1.jpg', cv2.IMREAD_GRAYSCALE)
img2=cv2.imread('C:/computervision/chap06/image/img2.jpg', cv2.IMREAD_GRAYSCALE)
if img1 is None or img2 is None : raise Exception("이미지읽기 오류")
img1=img1[100:500, 100:500]
img2=img2[100:500, 300:700]
cv2.namedWindow('dst')

def image1(value):
    pass
def image2(value):
    pass

alpha, beta = 50, 50

add_img = cv2.addWeighted(img1, alpha/100, img2, beta/100, 0)
dst=np.zeros((img1.shape[0], img1.shape[1]*3), np.uint8)
dst[:400, :400]=img1[:400, :400]
dst[:400, 400:800]=img2[:400, :400]
    
cv2.createTrackbar('img1', 'dst', alpha, 100, image1)
cv2.createTrackbar('img2', 'dst', beta, 100, image2)

while True:
    if cv2.waitKey(30) >=0: break

    alpha = cv2.getTrackbarPos('img1', 'dst')
    beta = cv2.getTrackbarPos('img2', 'dst')
    add_img = cv2.addWeighted(img1, alpha/100, img2, beta/100, 0)
    dst[:400, 800:1200]=add_img[:400, :400]
    cv2.imshow('dst', dst)