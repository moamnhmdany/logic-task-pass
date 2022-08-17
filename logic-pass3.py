from tokenize import String

from numpy import char


def findRepeatedChar(word:String,letter:char):
    counter:int = 0
    for initialNum in range(0,len(word)):
        if word[initialNum] == letter:
            counter += 1
    print(counter)

findRepeatedChar("moamn",'m')
