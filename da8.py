import random

def fourBitStrings(n):
    with open('fourBits.txt', 'w') as fl:
        for i in range(n):
            fl.write(format(random.randint(1,16),'04b') + '\n')

def makeStrings(numbits = 4, numstrings = 10, fl = 'myFile.txt'):
    with open(fl, 'w') as outfile:
        for i in range(numstrings):
            outfile.write(format(random.randint(1,2**numbits),'0' + str(numbits) + 'b') + '\n')

def eightBits(n=8):
    if n > 256 or n < 0:
        raise ValueError('Error: value out of range')
    with open('nBits.txt','w') as fl:
        for i in range(n):
            fl.write(format(i,'08b') + '\n')

if __name__ == '__main__':
    fourBitStrings(10)
    makeStrings(8, 3)
    eightBits(256)
