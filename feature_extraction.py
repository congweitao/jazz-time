import cv2
import numpy as np
from matplotlib import pyplot as plt
'''
a flow of 3d reconstruction from multiple images: image init -> feature extraction 
-> feature matching -> stitching/constructing -> dense -> meshing -> texturing -> publish
'''

image = cv2.imread('./images/woman-model-makeup-brunette.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fast = cv2.FastFeatureDetector_create()
kp = fast.detect(image, None)
img2 = cv2.drawKeypoints(image, kp, None, color=(255, 0, 0))

cv2.imshow('rbg', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

