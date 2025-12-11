import numpy as np
import pywt
import cv2

def w2d(img,mode = 'haar',level = 1):
    imArray = img
    imArray = cv2.cvtColor(imArray,cv2.COLOR_RGB2GRAY)
    # Converting to gray for single channel processing
    imArray = np.float64(imArray)
    imArray /= 255
    # Normalizes to [0,1]
    coeff = pywt.wavedec2(imArray,wavelet = mode,level = level)
    #print(coeff)
    # Applies 2d decomposition and returns a list

    coeff_h = list(coeff)
    coeff_h[0] *= 0
    # Sets the approximation (low_frequency) to zero

    imArray_h = pywt.waverec2(coeff_h,mode) # Reconstruction
    imArray_h *= 255
    imArray_h = np.uint8(imArray_h)

    return imArray_h