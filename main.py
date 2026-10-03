import cv2 as cv
import numpy as np

#   R G B A
#   VVVVVVVV
# 0xFFFFFFFF
canvas = np.zeros((512, 512, 3), np.uint8)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(canvas, "Test", (0, 256), font, 3, (255, 255, 255), 10)
cv.line(canvas, (0,0), (511,511), (255,0,0), 5)
cv.circle(canvas,(447,63), 63, (0,0,255), -1)
cv.rectangle(canvas, (384,0) ,(510,128), (0,255,0), 3)
cv.putText(canvas, "OpenCV",(10,500), font, 4, (255,255,255), 3, cv.LINE_AA)
pts = np.array([[10,5], [20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(canvas,[pts],True,(0,255,255))
cv.ellipse(canvas,(256,256),(100,50),0,0,180,255,-1)
cv.imshow("Test Window", canvas)
cv.waitKey(0)