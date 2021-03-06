def anagrams(string1, string2):
    string1 = sorted([letter for letter in string1 if letter.isalpha()])
    string2 = sorted([letter for letter in string2 if letter.isalpha()])
    if string1 == string2:
        return True
    else:
        return False

def runLengthEncoding(char_list):
    rle = []
    counter = 1
    # start at the second item and iterate through
    for i in range(1, len(char_list)):
        if char_list[i] == char_list[i-1]:
            # is the char at ith index same as prior?
            # if so, increment the counter and move to next item
            counter += 1
        else:
            # we've encountered a new item, so add the prior item and count
            # to the returned list and reset counter
            rle.append(char_list[i-1])
            rle.append(counter)
            counter = 1
    rle.append(char_list[-1]) # add the last char in the list
    rle.append(counter)
    return rle


def palindrome(x):
    x = x.split(' ')
    x = ''.join(x)
    x = [letter.lower() for letter in x if letter.isalpha()]
    y = x.copy()
    x.reverse()
    palind = True
    for i in range(len(x)):
        if x[i] != y[i]:
            return False
    return palind

if __name__ == '__main__':
    print(anagrams('cinema','iceman'))
    print(anagrams('hello','world'))
    print(anagrams('allow','wala'))
    print(runLengthEncoding(['a','a','a','b','b','a','c','c','b','b']))
    print(palindrome('racecar'))
    print(palindrome('a man a plan a canal panama!'))
    print(palindrome('    A m7a=9n==a7p9lAN   34$AcAN73aLP``aN9 aM   a  872')) 
    print(palindrome('this is not a palindrome')) 
