from scipy.misc import imread
import numpy as np

im = imread("farm.jpg")

col, row = im.size

data = np.zeros((row*col, 5))

pixels = im.load()

for i in range(row):

    for j in range(col):

        r, g, b = pixels[i, j]
        data[i*col + j, :] = r, g, b, i, j
