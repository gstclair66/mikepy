def maxValueInFile(filename):
    file=open(filename)
    List=[]
    
    for line in file:
        strippedline=int(line.strip())
        List.append(strippedline)
    file.close()
    return max(List)
   
   
def sumOfSquares(filename):
    file=open(filename)
    List=[]
    
    for line in file:
        strippedline=int(line.strip())
        List.append(strippedline)
    file.close()
    
    bList= [e ** 2 for e in List]
    return sum(bList)

def greaterThanN(filename,n):
    file=open(filename)
    List=[]
    
    for line in file:
        strippedline=int(line.strip())
        List.append(strippedline)
    file.close()
    
    if (n <= 750 and n >= -750):
        counter=0
        for element in List:
            if (element > n):
                counter+=1
        return counter
    else:
        return "Your integer is out of range."