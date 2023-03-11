import cv2
import numpy as numpy
img = cv2.imread('stones.jpg',cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("HelloWord")
cv2.imshow('Hello word,',img)
cv2.waitKey()