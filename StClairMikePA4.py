def getHawkId():
    return ["mmshkf"]

def AmIDigits(aList):
    if all([str(i).isdigit() for i in aList]):
        return ''.join(map(str,aList))
    else:
        return f'The length of the input is {len(aList)}.'
    
def findLetters(myList,myString):
    index = {c:False for c in myString}
    for value in myList:
        for character in value:
            if character in index:
                index[character]=True
    return all(index[s] for s in index)


def finalFunction(myList,n):
    if n < 0:
        newList=[0] * abs(n)
        print(newList)
    elif n == 0:
        return myList[-1]
    elif n > 0:
        return sum(myList)
    
