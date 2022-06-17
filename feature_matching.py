import cv2
import numpy as np
from matplotlib import pyplot as plt
'''
a flow of 3d reconstruction from multiple images: image init -> feature extraction 
-> feature matching -> stitching/constructing -> dense -> meshing -> texturing -> publish
'''

image1 = cv2.imread('./images/datac/IMG_1024.jpg')
image2 = cv2.imread('./images/datac/IMG_1026.jpg')
orb = cv2.ORB_create()

# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(image1,None)
kp2, des2 = orb.detectAndCompute(image2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1,des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
# Draw first 10 matches.
img3 = cv2.drawMatches(image1,kp1,image2,kp2,matches[:10],None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv2.imshow('rbg', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

