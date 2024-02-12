import numpy as np, cv2

def calc_spectrum(complex):
    if complex.ndim==2:
        dst = abs(complex)
    else:
        dst = cv2.magnitude(complex[:, :, 0], complex[:, :, 1])
    dst = cv2.log(dst + 1)
    cv2.normalize(dst, dst, 0, 255, cv2.NORM_MINMAX)
    return cv2.convertScaleAbs(dst)

def fftshift(img):
    dst = np.zeros(img.shape, img.dtype)
    h, w = dst.shape[:2]
    cy, cx = h//2, w//2
    dst[h-cy:, w-cx:] = np.copy(img[0:cy, 0:cx])
    dst[0:cy, 0:cx] = np.copy(img[h-cy:, w-cx:])
    dst[0:cy, w-cx:] = np.copy(img[h-cy:, 0:cx])
    dst[h-cy:, 0:cx] = np.copy(img[0:cy, w-cx:])
    return dst

image = cv2.imread("c:/computervision/chap09/image/1.jpg", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("이미지 읽기 오류")

dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
spectrum = calc_spectrum(fftshift(dft))
idft = cv2.idft(dft, flags=cv2.DFT_SCALE)[:,:,0]

cv2.imshow('spectrum', spectrum)
cv2.waitKey()
