def cadd(tups, tups2):
    first, last = tups
    first2, last2 = tups2
    return ((first + first2), (last + last2))

def cmult(tups, tups2):
    first, second = tups
    first2, second2 = tups2
    return ((first*first2 - second2*second), (first*second2 + second*first2))

def toComplex(x, y):
    return x + y*1j

def fromComplex(x):
    print(x.real)
    print(x.img)


z = cadd((1, 23), (4, 1))
stuff = toComplex(1,3)
print(stuff)
# print(fromComplex(1+3j))

print("ANswer : " + str(cmult((1,2),(2,24))))

print(cmult((3,4), (4,3)))
