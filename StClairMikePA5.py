def anagrams(string1,string2):
    #sorted function sorts both strings and then they are compared to check if
    #order is the same
    if(sorted(string1)==sorted(string2)):
        return True
    else:
        return False

def encode(myList):
    #determine length of list, set i=0, make empty list aList
    listlength = len(myList)
    i = 0
    aList = []
    #iterate through from 0 to length of the list
    while i < listlength:
        count = 1
        c = myList[i]
        i += 1
    #count number of repeated elements in a row in list
        while i < listlength and myList[i] == c:
            count += 1
            i += 1
    #condition for only 1 count of element
        if count == 1:
            aList += [c, count]
    #condition for everything else
        else:
            aList += [c, count]
    return aList

def isPalindrome(myString):
    #[::-1] means start at the end of the string and end at position 0, move with
    #the step -1, which means one step backwards
    if myString == myString[::-1]:
        return True
    else:
        return False


