from operator import mul
from functools import reduce


def problem1(n):
    return sum([i*i for i in range(n+1)])

def problem2(slope, intercept, x):
    return (slope * x) + intercept 

def problem3(aList):
    new_list = []
    for item in aList:
        new_list.append(item)
        new_list.append(item)
    return new_list

def problem4(list1, list2):
    acc = acc2 = 1
    for item in list1:
        acc = acc * item
    for item in list2:
        acc2 = acc2 * item
    return list1 if acc > acc2 else list2

def problem4v2(list1, list2):
    acc1 = reduce(mul, list1) 
    acc2 = reduce(mul, list2)
    return list1 if acc1 > acc2 else list2

if __name__ == '__main__':
    print(problem1(4))
    print(problem2(5,2,3))
    print(problem3([1,2,3]))
    print(problem4([1,2,3,4,5,6,7,8],[0,4,6,8,10,12,14,16,18,20]))
    print(problem4v2([1,2,3,4,5,6,7,8],[0,4,6,8,10,12,14,16,18,20]))
