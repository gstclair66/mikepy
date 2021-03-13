import random

def create_bin_number(length=8):
    digits = ''.join([str(random.choice([1,0])) for x in range(length)])
    return digits

def eightBitStrings(numdigits=5):
    fl = open('eightBits.txt','w')
    for i in range(numdigits):
        eightBitNum = create_bin_number(8)
        fl.write(eightBitNum  + '\n')
    fl.close()

def randomCharacters(n, myString):
    fl = open('nCharacters.txt', 'w')
    for i in range(n):
        fl.write(random.choice(myString) + '\n')
    fl.close()
    
def changeTheCase(myFile, case):
    if case not in ['upper','lower']:
        raise ValueError('Invalid Parameter - should be "upper" or "lower"')
    case_map = {'upper': lambda x: x.upper(),
                'lower': lambda x: x.lower()}
    outfile_name = "{}Case.txt".format(case)
    out_message = "Converted file to {} case".format(case)
    fl = open(myFile, 'r')
    fl_contents = fl.read()
    fl_contents = case_map[case](fl_contents)
    with open(outfile_name, 'w') as outfile:
        outfile.write(fl_contents)
    print(out_message)
    
    
    
if __name__ == '__main__':
    eightBitStrings()
    randomCharacters(5, 'The quick brown fox jumps over the lazy dog.')
    #changeTheCase('hello','poop')
    changeTheCase('testfile.txt', 'upper')
    changeTheCase('testfile.txt', 'lower')