# -*- coding: utf-8 -*-
"""
Created on Thu May 26 02:49:16 2016

@author: LENOVO
"""
import cv2
vidcap = cv2.VideoCapture('VID3.mp4')
success, image = vidcap.read()
count = 0
while success:
    success, image = vidcap.read()
    cv2.imwrite('v3/frame%d.jpg' % count, cv2.resize(image, (0, 0), fx=0.3, fy=0.3))     # save frame as JPEG file
    if cv2.waitKey(10) == 27:                     # exit if Escape is hit
        break
    count += 1
