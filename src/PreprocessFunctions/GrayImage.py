import cv2
from matplotlib import pyplot as plt
def grayImage(image):
    #plt.imshow(image)
    #plt.show()
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayImage = cv2.threshold(grayImage, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return grayImage