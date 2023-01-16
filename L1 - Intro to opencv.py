import cv2

frame = cv2.imread('Desktop/inofb18thwl31.jpg', 0)
frame = cv2.resize(frame, (0, 0), fx= 0.5, fy= 0.5) #resize frame
# frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE) #rotate frame
cv2.imshow('siyeon', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()