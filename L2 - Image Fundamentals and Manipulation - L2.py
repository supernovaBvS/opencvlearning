import cv2
import random

img = cv2.imread('/Users/dev/Desktop/inofb18thwl31.jpg', 1)

#manuiplating image pixels
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# print(img.shape)
# tag = copy and pasting parts of image
tag = img[350:500, 600:800]
img[100:250, 650:850] = tag

cv2.imshow('siyeon', img)
cv2.waitKey(0)
cv2.destroyAllWindows()