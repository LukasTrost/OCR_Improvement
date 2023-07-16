import cv2
import os
import pytesseract
import matplotlib.pyplot as plt
from src.DataFetchFunctions.FetchImagesAndGroundTruth import FetchImagesAndGroundTruth
from src.DataFetchFunctions.PerformOCRonYOLOCrops import PerformOCRonYOLOCrops
from src.PreprocessFunctions.CannyEdge import cannyEdgeDetection, dilatedCannyEdgeDetection
from src.PreprocessFunctions.GrayImage import grayImage, dilatedGrayImage, erodedGrayImage

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
print(current_directory)

input_Path = os.path.join(current_directory, "Normal/test")
output_path = os.path.join(current_directory, "Normal/results")
tesseract_save_path = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
functions = ["None",grayImage, cannyEdgeDetection, dilatedCannyEdgeDetection, dilatedGrayImage, erodedGrayImage]

YoloCrop_input_Path = os.path.join(current_directory, "Crop/crops")
YoloCrop_output_path = os.path.join(current_directory, "Crop/results")

if __name__ == '__main__':

    # use this to perform normal ocr
    #FetchImagesAndGroundTruth(input_Path,output_path, functions, tesseract_save_path, output_detected_text = True)

    #use this to perform ocr on cropped out images
    #PerformOCRonYOLOCrops(YoloCrop_input_Path,YoloCrop_output_path, functions, tesseract_save_path, output_detected_text = False)
