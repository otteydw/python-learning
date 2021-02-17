import numpy as np
import cv2

# cap = cv2.VideoCapture(0)

def testDevice(source):
   cap = cv2.VideoCapture(source)
   if cap is None or not cap.isOpened():
       print('Warning: unable to open video source: ', source)

testDevice(0) # no printout
testDevice(1) # prints message
testDevice(2) # no printout
testDevice(3) # prints message
testDevice(4) # prints message