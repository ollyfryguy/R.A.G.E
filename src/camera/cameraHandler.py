import cv2
#from cv2_enumerate_cameras import enumerate_cameras
import numpy
import threading

arducamL = cv2.VideoCapture(0)
arducamR = cv2.VideoCapture(1)

if not arducamL.isOpened() or not arducamR.isOpened():
    print("ERROR: Could not open camera")

while True:
    recievedL, lFrame = arducamL.read()
    recievedR, rFrame = arducamR.read()
    
    if not recievedL or not recievedR:
        print("Didn't recieve frame. Exiting...")
        break
    
    hStackFrame = cv2.hconcat([lFrame, rFrame])
    
    cv2.imshow('Horizontally Stacked Frame', hStackFrame)
    if cv2.waitKey(0):
        break


arducamL.release()
cv2.destroyAllWindows()