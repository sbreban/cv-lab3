import cv2
import numpy as np

# img = cv2.imread('MorpologicalCornerDetection.png', 0)
img = cv2.imread('square-rectangle.png', 0)

cross = np.array([
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]], dtype=np.uint8)
diamond = np.array([
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0]], dtype=np.uint8)
r1 = cv2.dilate(img, cross, iterations=1)
r1 = cv2.erode(r1, diamond, iterations=1)

xshape = np.array([
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1]], dtype=np.uint8)
square = np.array([
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]], dtype=np.uint8)
r2 = cv2.dilate(img, xshape, iterations=1)
r2 = cv2.erode(r2, square, iterations=1)
r = cv2.absdiff(r2, r1)
# grab the image dimensions
h = r.shape[0]
w = r.shape[1]

# loop over the image, pixel by pixel
for x in range(0, h):
    for y in range(0, w):
        # threshold the pixel
        if r[x, y] > 50:
            cv2.circle(img, (y, x), 5, (255, 0, 0))
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
