import cv2
import pytesseract
import matplotlib.pyplot as plt
from src.DataFetchFunctions.FetchImagesAndGroundTruth import FetchImagesAndGroundTruth
from src.PreprocessFunctions.CannyEdge import cannyEdgeDetection
from src.PreprocessFunctions.GrayImage import grayImage

input_Path = "D://Programmieren//MasterOfDisaster//Implementierungen//OCR//Images//train"
output_path = "D://Programmieren//MasterOfDisaster//Implementierungen//OCR//Images//"
tesseract_save_path = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
functions = ["None", cannyEdgeDetection, grayImage]

if __name__ == '__main__':
    FetchImagesAndGroundTruth(input_Path,output_path, functions, tesseract_save_path)
