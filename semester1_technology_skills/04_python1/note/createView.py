import sys

def main():
    sourceFileName = getFileNameFromCommandLine()
    sourceFile = open(sourceFileName, "r")
    isSpeakerView = checkSpeakerView(sourceFile)
    # create output file depending on value of speaker view
    outputFile = open(f"{sourceFileName}_converted.md", "w")
    convertInputFile(sourceFile, outputFile, isSpeakerView)
    # close all files
    sourceFile.close()
    outputFile.close()

def getFileNameFromCommandLine():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    else:
        return sys.argv[1]

def checkSpeakerView(sourceFile):
    firstLine = sourceFile.readline()
    if (firstLine.find("SPEAKER_VIEW") != -1):
        if firstLine.find("TRUE") != -1:
            return True
        else:
            return False
    else:
        print("Error speaker config var not found in first line of source file")
        sys.exit(1)

def convertInputFile(sourceFile, outputFile, isSpeakerView):
    for line in sourceFile:
        if containsComment(line):
            if isSpeakerView:
                if "<!--- Include:" in line:
                    pythonSrcFileName = line.replace("<!--- Include: ", "").replace("--->", "").strip()
                    pythonSrcFile = open(pythonSrcFileName, "r")
                    outputFile.write("## Demo Code begin\n")
                    outputFile.write("```python\n")
                    outputFile.write(pythonSrcFile.read())
                    outputFile.write("```\n")
                    outputFile.write("## Demo Code end\n")
                    pythonSrcFile.close()
                else:
                    # just print the comment as is
                    outputFile.write(line)
        else:
            outputFile.write(line)

def containsComment(line):
    if (line.find("<!---") != -1):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
