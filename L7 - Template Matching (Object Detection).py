import cv2
import numpy as np

img = cv2.imread('/Users/dev/Desktop/union_work/opencvlearning/train/soccer_practice.jpg', 0)
tem = cv2.imread('/Users/dev/Desktop/union_work/opencvlearning/train/shoe.png', 0)
h, w = tem.shape
# print(img)
# (height, width, channels)

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    res = cv2.matchTemplate(img2, tem, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        loc = min_loc
    else:
        loc = max_loc

    bot_right = (loc[0] + w, loc[1] + h)
    cv2.rectangle(img2, loc, bot_right, 255, 5)
    cv2.imshow('football', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 