import pytesseract
from matplotlib import pyplot as plt
import numpy as np
import cv2
import Levenshtein

def apply_masks(string, mask_sizes):
    for i in range(len(string)):
        for mask_size in mask_sizes:
            if i + mask_size <= len(string):
                substring = string[i:i+mask_size]
                print(substring)


def applyOCR(image, tesseract_save_path, output_detected_text):
    #print(image)
    #plt.imshow(image)
    #plt.show()
    pytesseract.pytesseract.tesseract_cmd = tesseract_save_path
    synonyms = {
            "ABC-Powder" : ["abc", "abc-pulver", "abc-powder"],
            "Foam": ["schaum", "foam",],
            "Metal-Powder" : ["metall"],
            "CO2" : ["c02", "co2", "kohlendioxid", "kohlen", "carbon", "carpon", "dioxid", ],
            "Water" : ["wasser", "water"],
            "Water-Solution" : ["water solution", "solution", "wässrige lösung"],
            "Wet-Chemical" : ["fat", "fett", "flüssig", "löschmittel", "flüssiglöschmittel"]
        }

    text = pytesseract.image_to_string(image, lang = "deu")
    text = text.lower()
    print(text)
    print("was the text")
    for i in range(len(text)):
        for word, synonym_list in synonyms.items():
            for synonym in synonym_list:
                len_synonym = len(synonym)
                if i + len_synonym <= len(text):
                    substring = text[i:i + len_synonym]
                    distance = Levenshtein.distance(substring, synonym)
                    similarity = 1 - (distance / max(len(substring), len(synonym)))
                    if similarity > 0.8:
                        print("chosen synonym: ", synonym,"therefore word", word," Because it found ",  substring)
                        return word, text
    return "None", text
