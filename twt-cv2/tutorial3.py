import numpy as np
import cv2

cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # cv2.imshow('frame', frame) # would show exact frame

    # Get dimensions of original frame
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # print(width, height)

    # Mirror the frame
    frame = cv2.flip(frame, 0)

    # Create a blank copy of the frame
    image = np.zeros(frame.shape, np.uint8)

    # Create a half-size copy of the frame
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    image[:height//2, :width//2] = smaller_frame    # Copy image to top-left corner of frame
    image[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)    # Copy image to bottom-left corner of frame
    image[:height//2, width//2:] = smaller_frame    # Copy image to top-right corner of frame
    image[height//2:, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)    # Copy image to bottom-right corner of frame
    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()