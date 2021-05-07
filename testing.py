import cv2 as cv2
import numpy as np
import sys
from pyrUp import *
from pyrDown import *
from subtract import *


img = np.float32([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
#img = np.float32([[1, 2], [3, 4]])
#img = np.float32([[2, 2], [2, 2]])


funcResult = pyrDown(img)
print("my PyrDown")
print(funcResult)

funcResult = cv2.pyrDown(img)
print("cv2 PyrDown")
print(funcResult)

funcResult = pyrUp(img)
print("my PyrUp")
print(funcResult)

funcResult = cv2.pyrUp(img)
print("cv2 PyrUp")
print(funcResult)


# expanded = cv2.pyrUp(funcResult)
# laplace = cv2.subtract(img, expanded)
# print(laplace)
# laplace = subtract(img, expanded)
# print(laplace)
