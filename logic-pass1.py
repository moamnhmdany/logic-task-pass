from tokenize import String
from turtle import end_fill
from unicodedata import name

from numpy import array


def  removeChar( string1,char)-> String:
    editString =""
    for initialValue in  range(0,len(string1)) :
        if string1[initialValue] != char:
            editString += string1[initialValue]
    return editString           
                    

word =removeChar("ABCDE", "C")
print(word)
