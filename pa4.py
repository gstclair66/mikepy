def AmIDigits(aList):
    try:
        answer =  int("".join([str(i) for i in aList]))
    except ValueError:
        answer =  "The length of the input is " + str(len(aList))
    return answer

def findLetters(myList, myString):
    allletters = "".join([str(i) for i in myList]).upper()
    answer = True
    for letter in myString:
        if letter.upper() not in allletters:
            return False
    return answer

def finalFunction(myList, n):
    if n < 0:
        num_zeros = abs(n)
        zero_list = []
        for i in range(num_zeros):
            zero_list.append(0)
        return [myList, zero_list]
    elif n == 0:
        return myList[-1]
    else:
        return sum(myList)

if __name__ == '__main__':
    print(AmIDigits([6,'hello']))
    print(AmIDigits(["hello",23]))
    print(AmIDigits(["10","111"]))
    print(AmIDigits(["123",4,5,6,7]))
    print(AmIDigits(['123','456','789']))
    print(findLetters(["Hello","World"],"hold"))
    print(findLetters(["Hello","World"],"down"))
    print(finalFunction([1,2,3],-2))
    print(finalFunction([1,2,3],0))
    print(finalFunction([1,2,3],5))
