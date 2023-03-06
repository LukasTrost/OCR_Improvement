import cv2
def canny(img, blurParameters, cannyParameters):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, blurParameters, 0)
    canny = cv2.Canny(blur, cannyParameters[0], cannyParameters[1])
    return canny
def cannyEdgeDetection(image):
    edges = canny(image, [5,5], [40,70])
    cannyEdgeImage = cv2.threshold(edges, 1, 10000, cv2.THRESH_BINARY)[1]
    return cannyEdgeImage