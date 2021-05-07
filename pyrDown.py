import numpy as np
import math
import sys


def pyrDown(img):

    #weight = np.array([1/256, 4/256, 6/256, 4/256, 1/256])
    weight = np.array([1, 4, 6, 4, 1])
    #weight = np.array([0.05, 0.25, 0.4, 0.25, 0.05])
    #weight = np.array([0.023792, 0.094907, 0.150342, 0.094907, 0.023792])

    #img = np.array(img)
    dimensions = np.shape(img)
    # height = dimensions[1]
    # width = dimensions[2]
    height = dimensions[0]
    width = dimensions[1]
    heightNew = math.ceil(height * 0.5)
    widthNew = math.ceil(width * 0.5)

    # padding rows
    I = [img[0, :]]
    I = np.append(I, [img[1, :]], axis=0)
    for i in range(height):
        I = np.append(I, [img[i, :]], axis=0)
    I = np.append(I, [img[height - 2, :]], axis=0)
    I = np.append(I, [img[height - 1, :]], axis=0)

    img = I.copy()

    # padding columns
    I = [img[:, 0]]
    I = np.transpose(I)

    I = np.append(I, np.transpose([img[:, 1]]), axis=1)

    for i in range(width):
        I = np.append(I, np.transpose([img[:, i]]), axis=1)
    I = np.append(I, np.transpose([img[:, width - 2]]), axis=1)
    I = np.append(I, np.transpose([img[:, width - 1]]), axis=1)

    IResult = np.zeros((heightNew, widthNew))

    for i in range(heightNew):
        for j in range(widthNew):
            A = np.float32([])
            for m in range(-2, 3):
                for n in range(-2, 3):
                    tmpval = I[2 * i + m + 2, 2 * j + n + 2] * \
                        weight[m + 2] * weight[n + 2]
                    A = np.append(A, tmpval)
            IResult[i, j] = np.sum(A)/256

    return IResult
