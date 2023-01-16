
import cv2

# cap = cv2.VideoCapture(0)
# print("Cam Opened:", cap.isOpened())
# while(True):
    # Capture frame-by-frame
    # ret, frame = cap.read()
    # cv2.imshow('frame',frame)
    # cv2.waitKey(1)
    # if cv2.waitKey(1) & 0xFF == ord('Q'):
    #     break
    # elif cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()



frame = cv2.imread('Desktop/inofb18thwl31.jpg', 0)
frame = cv2.resize(frame, (0, 0), fx= 0.5, fy= 0.5) #resize frame
# frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE) #rotate frame
cv2.imshow('siyeon', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()