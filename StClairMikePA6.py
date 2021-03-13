import random

def eightBitStrings(n):
    eightBits = "eightBits.txt"
    outputFile = open(eightBits,"w")

    for element in range(n):
        # create our string and we will randomly select 0 or 1 eight times
        s = ""
        for i in range(8):
            # randomly generate 0 or 1 and append to our string
            randomNum = int(random.random()*2)
            s = s + str(randomNum)

        # output to file
        outputFile.write(s+"\n")        

    outputFile.close()
    
def randomCharacters(n,myString):
    nCharacters="nCharacters.txt"
    outputFile=open(nCharacters,"w")
    newString=myString.replace(" ","")
    for element in range(n):
        s=""
        randlet=random.choice(newString)
        s=s+str(randlet)
        outputFile.write(s+"\n")        

    outputFile.close()
    

def changeTheCase(myFile,case):
 
    if str(case) == "upper":
        upperCase="upperCase.txt"
        with open(myFile) as original, open(upperCase, "w") as upperfile:
            for line in original:
                upperfile.write(line.upper())
        return "Converted file to upper case."
    elif str(case) == "lower":
        lowerCase="lowerCase.txt"
        with open(myFile) as original, open(lowerCase, "w") as lowerfile:
            for line in original:
                lowerfile.write(line.lower())
        return "Converted file to lower case."
    else:
        return "Invalid parameter."
    
    