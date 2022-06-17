from PIL import Image
import pytesseract as pt
import cv2

img_file = '../corp-energy-china.jpg'
print('Opening Sample file using Pillow')
img_obj = cv2.imread(img_file)
img_obj_grey = cv2.cvtColor(img_obj, cv2.COLOR_BGR2GRAY)
print('Converting %s to string' % img_file)
ret = pt.image_to_string(img_obj_grey, lang='chi_sim')
print('Result is: ', ret)

