
def determineCorrectness(determinedLabel, groundTruth):

    if groundTruth == "Schaum" or groundTruth == "Foam":
        groundTruth = "Schaum"
    if groundTruth == "Pulver" or groundTruth == "powder" or groundTruth == "ABC-Pulver" or groundTruth == "ABC-Powder":
        groundTruth = "ABC-Pulver"
    if groundTruth == "Kohlendioxid" or groundTruth == "CO2":
        groundTruth = "Kohlendioxid"
    if groundTruth == "Wasser" or groundTruth == "Water":
        groundTruth = "Wasser"
    if groundTruth == "Wässrige Lösung" or groundTruth == "Water solution":
        groundTruth = "Wässrige Lösung"
    if groundTruth == "Fettbrandschaum" or groundTruth == "FatWaterSolution":
        groundTruth = "Fettbrandschaum"

    if determinedLabel == groundTruth:
        return True
    else:
        return False