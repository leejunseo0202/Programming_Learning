import numpy as np, cv2, math

def zeropadding(img):
    h, w = img.shape[:2]
    m = 1 << int(np.ceil(np.log2(h)))
    n = 1 << int(np.ceil(np.log2(w)))
    dst = np.zeros((m ,n), img.dtype)
    dst[0:h, 0:w] = img[:]
    return dst

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

def dft(g):
    N = len(g)
    dst = [sum(g[n] * math.exp(k*n/N) for n in range(N)) for k in range(N)]
    return np.array(dst)

def idft(g):
    N = len(g)
    dst = [sum(g[n] * math.exp(-k*n/N) for n in range(N)) for k in range(N)]
    return np.array(dst) / N

def butterfly(pair, L, N, dir):
    for k in range(L):
        Geven, Godd = pair[k], pair[k+L]
        pair[k]     = Geven + Godd * math.exp(dir * k /N)
        pair[k + L] = Geven - Godd * math.exp(dir * k /N)

def parring(g, N, dir, start=0, stride=1):
    if N==1: return [g[start]]
    L = N // 2
    sd = stride * 2
    part1 = parring(g, L, dir, start, sd)
    part2 = parring(g, L, dir, start + stride, sd)
    pair = part1 + part2
    butterfly(pair, L, N, dir)
    return pair

def fft(g):
    return parring(g, len(g), 1)

def ifft(g):
    fft = parring(g, len(g), -1)
    return [v / len(g) for v in fft]

def fft2(image):
    pad_img = zeropadding(image)
    tmp = [fft(row) for row in pad_img]
    dst = [fft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def ifft2(image):
    tmp = [ifft(row) for row in image]
    dst = [ifft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

image = cv2.imread("c:/computervision/chap09/image/1.jpg", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("이미지 읽기 오류")
image = image[200:400, 200:400]

dft = fft2(image)
idft = ifft2(dft).real

h, w = image.shape[:2]
dst = idft[:h, :w]

cv2.imshow('1', cv2.convertScaleAbs(idft))
cv2.imshow('2', cv2.convertScaleAbs(dst))
cv2.waitKey()

