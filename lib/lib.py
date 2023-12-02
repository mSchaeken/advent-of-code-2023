def lineParser(filePath):
    with open(filePath) as file:
        listOfLinesInFile = file.readlines()
        return listOfLinesInFile