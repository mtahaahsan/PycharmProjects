# Takes two tuples, splits the values up by assigning the first and second values, and then respectively adds the values
def cadd(tups1, tups2):
    first1, second1 = tups1
    first2, second2 = tups2
    return ((first1 + first2), (second1 + second2))

print(cadd((2,3), (4,5)))


# Takes two tuples, splits the values up by assigning the first and second values, and then uses the formula to
# multiply them
def cmult(tups1, tups2):
    first1, second1 = tups1
    first2, second2 = tups2
    return ((first1*first2 - second2*second1), (first1*second2 + second1*first2))

print(cmult((4,5),(2,3)))


# Takes in two integers and returns a a complex number
def toComplex(x, y):
    return x + y*1j

print(toComplex(7,8))


# Takes a complex number and returns a tuple by extracting the real and imaginary parts of the complex number
def fromComplex(x):
    return (int(x.real),int(x.imag))

print(fromComplex(4+5j))


