import numpy as np, cv2

# def calc_histo(image, channels, bsize, ranges):
#     shape = bsize if len(channels) >1 else(bsize[0], 1)
#     hist = ()
#     gap = np.divide(ranges[1::2], bins)
#
#     for row in ():
#         for val in ():
#             idx = np.divide(val[channels], gap).astype('uint')
#             hist[tuple(idx)]+=1
#
#     return hist

image = cv2.imread("c:/computervision/chap06/image/img1.jpg")
if image is None : raise Exception("영상파일 읽기 오류")
image=image[200:500,200:500]

hist = cv2.calcHist([image], [0], None, [256], [0,256])
cv2.normalize(hist, hist, 0, image.shape[0], cv2.NORM_MINMAX)


print(hist.flatten())
