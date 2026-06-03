import cv2
import numpy
import threading

defaultWidth = 1920
defaultHeight = 1080

class VideoStream:
    def __init__(self, width, height):
            self.width = width
            self.height = height

            if height == None or width == None:
                 self.height = defaultHeight
                 self.width = defaultWidth
    
    def testValues(self):
        print(self.width)
        print(self.height)



cameraStream = VideoStream(None, None)

cameraStream.testValues