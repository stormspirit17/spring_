import numpy
import cv2
vidcap = cv2.VideoCapture('VID2.mp4')
success, image = vidcap.read()
count = 0
while success:
    success, image = vidcap.read()
    cv2.imwrite('v2/frame%d.jpg' % count, cv2.resize(image, (0, 0), fx=0.3, fy=0.3))     # save frame as JPEG file
    if cv2.waitKey(10) == 27:                     # exit if Escape is hit
        break
    count += 1
