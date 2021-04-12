def checkFormat(n):
    if (str(n).isdigit() == True):
        if (len(str(n)) == 13):
            return True
        else:
            return False
    else:
        return False
        
def calculateCheckDigit(n):
    n = str(n)
    if not len(n) == 12:
        return -99
    else:
        relevant_chars = n[:12]
        calc_result = []
        # if index is even, multiply value by 3 else 1
        for index in range(1, len(relevant_chars) + 1):
            if index % 2 == 0:
                calc_result.append(int(relevant_chars[index - 1]) * 3)
            else:
                calc_result.append(int(relevant_chars[index - 1]))
        # sum the results        
        sum_relevant_chars = sum(calc_result) 
        # find the modulo 10
        mod_10 = sum_relevant_chars % 10
        # if the mod 10 is 0, return 0 else 10 - the mod 10
        calc_checkdigit = (10 - mod_10) if mod_10  > 0 else 0
        return calc_checkdigit
    
def validISBN(n):
    # checks if the last digit of a 13-digit ISBN is valid 
    # first 12 indexs of 13-index ISBN
    if not checkFormat(n):
        return False
    else:
        n = str(n)
        check_digit = int(n[-1])
        relevant_chars = n[:12]
        calc_result = calculateCheckDigit(relevant_chars)
        if calc_result != -99:
            return True if calc_result == check_digit else False
        else:
            return 'bad ISBN format'
   
def flipBits(myString):
    if len(myString) != 8: return "wrong length"
    bit_container = []
    for item in myString:
        if int(item) != 0 and int(item) != 1:
            return "not a binary string"
        #flip the bit using "not" operator
        bit_container.append(int(not int(item)))
    return ''.join([str(item) for item in bit_container])    

def xor(string1, string2):
    if len(string1) != 4 and len(string2) != 4:
        return 'wrong length'
    all_string = string1 + string2
    for item in all_string:
        if int(item) != 1 and int(item) != 0:
            return "not a binary string"
    bit_container = []
    string_result = ""
    for item in zip(string1, string2):
        bit_container.append(item)
    # '^' is the xor operator in python    
    for item in bit_container:    
        string_result += str((int(item[0]) ^ int(item[1])))
    return string_result    





if __name__ == '__main__':
   print(validISBN(9781861972712))
   print(validISBN('9781861972712'))
   print(calculateCheckDigit(978186197271))
   print(flipBits('11001010'))
   print(xor("1100","1010"))
