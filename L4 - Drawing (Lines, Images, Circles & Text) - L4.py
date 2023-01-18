import numpy as np
import cv2

cap = cv2.VideoCapture(1)
print("Cam Opened:", cap.isOpened())
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 20)
    img = cv2.rectangle(img, (0, 0), (width, height), (0, 0, 255), 30)
    img = cv2.circle(img, (300, 300), 60, (255, 0, 255), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img - cv2.putText(img, "收工未啊我? :(", (200, height -10), font, 4, (0, 255, 255), 5, cv2.LINE_AA)

    cv2.imshow('frame',img)
    # cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()