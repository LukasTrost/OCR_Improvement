import cv2
import pytesseract
import numpy as np
from matplotlib import pyplot as plt
def grayImage(image):
    #plt.imshow(image)
    #plt.show()
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayImage = cv2.threshold(grayImage, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return grayImage

def dilatedGrayImage(image):
    #plt.imshow(image)
    #plt.show()
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayImage = cv2.threshold(grayImage, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    kernel = np.ones((5, 5), np.uint8)
    dilatedGrayImag = cv2.dilate(grayImage, kernel, iterations=1)
    return dilatedGrayImag

def erodedGrayImage(image):
    #plt.imshow(image)
    #plt.show()
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayImage = cv2.threshold(grayImage, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    kernel = np.ones((5, 5), np.uint8)
    erodedGrayImag = cv2.erode(grayImage, kernel, iterations=1)
    return erodedGrayImag

def rotatedGrayImage(image):
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayImage = cv2.threshold(grayImage, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    #print(pytesseract.image_to_string(grayImage))
    osd = pytesseract.image_to_osd(grayImage)
    #print(osd)
    angle = int(osd.split('\n')[2].split(':')[-1])
    #print(angle)
    if angle != 0:
        center = tuple(np.array(grayImage.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(grayImage, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
        #plt.imshow(rotated)
        #plt.show()
    else:
        rotated = grayImage
    return rotated