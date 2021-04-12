
def flipBits(myString):
    if all(character in "01" for character in myString):
        if len(myString) == 8:
               newString=myString.replace('1','temp').replace('0','1').replace('temp','0')
               return newString
        else:
            return "wrong length"
    else:
        return "not a binary string"
    
def xor(string1,string2):
    if all(character in "01" for character in string1 and string2):
        if len(string1 and string2) == 4:
            return "{0:04b}".format(int(string1,2) ^ int(string2,2))
        else:
            return "wrong length"
    else:
        return "not binary strings"