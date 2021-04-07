import random
def Fourbits(n):
    Fourbits = "Fourbits.txt"
    outputFile = open(Fourbits,"w")

    for element in range(n):
        # create our string and we will randomly select 0 or 1 eight times
        s = ""
        for i in range(4):
            # randomly generate 0 or 1 and append to our string
            randomNum = int(random.random()*2)
            s = s + str(randomNum)

        # output to file
        outputFile.write(s+"\n")        

    outputFile.close()
    
def makeStrings(bits,strings,fileName):
    File = str(fileName)
    outputFile = open(File,"w")

    for element in range(strings):
        # create our string and we will randomly select 0 or 1 eight times
        s = ""
        for i in range(bits):
            # randomly generate 0 or 1 and append to our string
            randomNum = int(random.random()*2)
            s = s + str(randomNum)

        # output to file
        outputFile.write(s+"\n")        

    outputFile.close()
    
def eightBits(n):
    if 0 <= n <= 256:
        nBits = "nBits.txt"
        outputFile = open(nBits,"w")
        s="" 
        for i in range(0,n):
            s=s+format(i,'08b') +"\n"
        outputFile.write(s)
    
    else:
        return "Error: value out of range."
    outputFile.close()
  
        



