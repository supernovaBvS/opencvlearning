import cv2
import numpy as np

img = cv2.imread('/Users/dev/Desktop/Chess_Board.svg.png', 1)
img = cv2.resize(img, (0, 0), fx=0.55, fy=0.55)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)


for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)

# (x1, y1) (x2, y2)
# sqrt((x2-x1)**2 + (y2-y1)**2) //Euclidean equation

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()