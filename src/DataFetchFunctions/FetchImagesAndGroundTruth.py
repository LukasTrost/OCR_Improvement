import os
import cv2
from matplotlib import pyplot as plt
from src.OCRFunctions.OCR import applyOCR
from src.AccuracyCalculation.DetermineTruthAndSynonyms import determineCorrectness
import openpyxl
def FetchImagesAndGroundTruth(imagePath,outputPath, functions, tesseract_save_path):
    folders = os.listdir(imagePath)
    excelfile = openpyxl.Workbook()
    excelsheet = excelfile.active
    excelsheet.title = "Results"
    for idx,function in enumerate(functions):
        excelsheet.cell(column=idx+2, row=1, value = str(function))

    for folder in folders:
        groundTruth = folder
        folderPath = os.path.join(imagePath, folder)
        images = os.listdir(folderPath)
        for imgidx, imagename in enumerate(images):
            excelsheet.cell(column=1, row=imgidx, value=imagename)
            #print(os.path.join(folderPath,imagename))
            #print(os.path.exists(os.path.join(folderPath,imagename)))
            image = cv2.imread(os.path.join(folderPath,imagename))
            #plt.imshow(image)
            #plt.show()
            for fncidx,function in enumerate(functions):
                if function == "None":
                    processedImage = image
                else:
                    processedImage = function(image)
                calculatedLabel,labelWasDetermined = applyOCR(processedImage, tesseract_save_path)
                if labelWasDetermined:
                    wasCorrect = determineCorrectness(calculatedLabel,groundTruth)
                    if wasCorrect:
                        excelsheet.cell(column=fncidx + 2, row=imgidx + 2, value="Wrong Label determined")
                    else:
                        excelsheet.cell(column=fncidx + 2, row=imgidx + 2, value="correct")
                else:
                    excelsheet.cell(column=fncidx + 2, row=imgidx+2, value="No Label determined")
    counter = 2
    output = f'{os.path.join(outputPath,"Accuracy OCR.xlsx")}'
    while os.path.exists(output):
        output = f'{os.path.join(outputPath, "Accuracy OCR" + counter + ".xlsx")}'
        counter = counter + 1
    excelfile.save(output)
