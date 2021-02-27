

def problem2(aList):
    if len(aList) % 2 == 0:
        return sum(aList)
    else:
        for i, item in enumerate(aList):
            aList[i] = len(aList)
        return aList
    
def problem3(aList):
    bList = [aList ** 2 for aList in aList]
    return bList

def problem4(word):
    return word * len(word)