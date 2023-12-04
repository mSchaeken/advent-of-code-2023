def lineParser(filePath, stripNewlineChars):
    with open(filePath) as file:
        if stripNewlineChars == True:
            newLineCharsStripped = []
            for line in file.readlines():
                newLineCharsStripped.append(line.strip('\n'))
            return newLineCharsStripped
        return file.readlines()