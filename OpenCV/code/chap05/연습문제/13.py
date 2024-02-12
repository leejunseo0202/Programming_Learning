import numpy as np, cv2

def print_rects(rects):
        for i, (x, y, w, h, a) in enumerate(rects):
                print("rexts[%i] = [(%3d,%3d) from (%3d,%3d)] %5d" % (i, x, y, w, h, a))

rands = np.zeros((5,5), np.uint16)
starts = cv2.randn(rands[:,:2], 100, 50)
ends = cv2.randn(rands[:, 2:-1],300, 50)

sizes = cv2.absdiff(starts, ends)
areas = sizes[:,0] * sizes[:,1]
rects = rands.copy()
rects[:, 2:-1] = sizes
rects[:,-1]=areas

index = cv2.sortIdx(areas, cv2.SORT_EVERY_COLUMN).flatten()

print_rects(rects[index.astype('int')])