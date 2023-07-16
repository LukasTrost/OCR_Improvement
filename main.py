import cv2
import pytesseract
import matplotlib.pyplot as plt
from src.DataFetchFunctions.FetchImagesAndGroundTruth import FetchImagesAndGroundTruth
from src.DataFetchFunctions.PerformOCRonYOLOCrops import PerformOCRonYOLOCrops
from src.PreprocessFunctions.CannyEdge import cannyEdgeDetection, dilatedCannyEdgeDetection
from src.PreprocessFunctions.GrayImage import grayImage, dilatedGrayImage, erodedGrayImage


input_Path = "D://Programmieren//MasterOfDisaster//Experiments_and_Implementations//Labels//OCR//FELOD test//test"
output_path = "D://Programmieren//MasterOfDisaster//Experiments_and_Implementations//Labels//OCR//Results"
tesseract_save_path = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
functions = ["None",grayImage, cannyEdgeDetection, dilatedCannyEdgeDetection, dilatedGrayImage, erodedGrayImage]

YoloCrop_input_Path = "D://Programmieren//MasterOfDisaster//OCR Zwischenspeichern//Final Run"
YoloCrop_output_path = "D://Programmieren//MasterOfDisaster//OCR Zwischenspeichern//OCR//"

if __name__ == '__main__':

    # use this to perform normal ocr
    #FetchImagesAndGroundTruth(input_Path,output_path, functions, tesseract_save_path, output_detected_text = True)

    #use this to perform ocr on cropped out images
    #PerformOCRonYOLOCrops(YoloCrop_input_Path,YoloCrop_output_path, functions, tesseract_save_path, output_detected_text = False)
