def perfectSquares(n):
    myList=list(range(1,n+1))
    newList=[]
    
    for e in myList:
        e=e**2
        newList.append(e)
        
    return sum(newList)

def ycoord(m,b,x):
    y=int(m)*int(x)+int(b)
    return y

def listdoubler(myList):
    newList=[]
    for e in myList:
        newList.append(e)
        newList.append(e)
    return newList

def listcompare(List1,List2):
    result1=1
    result2=1
    for e in List1:
        result1=result1*e
    for e in List2:
        result2=result2*e
        
#     return result1,result2

    if result1>result2:
        return List1
    elif result2>result1:
        return List2
