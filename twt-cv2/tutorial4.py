import numpy as np
import cv2

cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Get dimensions of original frame
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # print(width, height)

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10) # Draw line from top left to bottom right
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 10) # Draw line from bottom left to top right
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5) # negative thickness would fill in completely
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'w00t!', (10, height-10), font, 2, (255, 255, 255), 5, cv2.LINE_AA)



    # cv2.imshow('frame', frame) # would show exact frame
    cv2.imshow('frame', img) # would show exact frame

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()