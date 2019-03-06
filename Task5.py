# Takes in input and converts it to string using the str() method, and then strips the string of any parenthasis
def encdat(x):
    myString = str(x)
    myString = myString.strip("(")
    myString = myString.strip(")")
    return myString

print(encdat(4+5j))
print(type(encdat(4+5j)))
