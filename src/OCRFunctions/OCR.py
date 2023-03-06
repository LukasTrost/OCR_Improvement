import pytesseract
def applyOCR(image, tesseract_save_path):
    pytesseract.pytesseract.tesseract_cmd = tesseract_save_path
    synonyms = {
            "ABC-Pulver" : ["abc", "abc-pulver", "abc-powder"],
            "Schaum": ["schaum", "foam",],
            "MetallPulver" : ["metall"],
            "Kohlendioxid" : ["c02", "co2", "kohlendioxid", "kohlen", "carbon"],
            "Wasser" : ["wasser", "water"],
            "Wässrige Lösung" : ["water solution", "solution", "wässrige lösung"],
            "Fettbrandschaum" : ["fat", "fett"]
        }
    text = pytesseract.image_to_string(image)
    text = text.lower()
    #print(text)
    word_indices = {}
    for word, synonym_list in synonyms.items():
        for synonym in synonym_list:
            index = text.find(synonym)
            if index != -1:
                word_indices[word] = index
    if not word_indices:
        return 'None', False
    else:
        first_word = min(word_indices, key=word_indices.get)
        #print(first_word)
        return first_word, True