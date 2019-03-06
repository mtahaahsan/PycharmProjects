#not a endless generator this will only get primes upto the passed input or 40000
def eratosthenes(z=40000):
    #create an array of true values the size of z
    A = [True] * z
    #iterate over each value to z squared
    for x in range(2, int(z**0.5)):
        #if A[x] has a true value
        if A[x]:
            #iterate over a range starting from x*2 ending at z in jumps of x
            for z in range(x * 2, z, x):
                #set anything in the range to false
                A[z] = False
    #iterate over the array
    for y in range(2, len(A)):
        #if a value is true that index is a prime number
        if A[y]:
            #yield the current iterator location as it is a prime
            yield y

#creates a instance of the generator and prints out 50 primes
pNumbers = eratosthenes()
for printer2 in range(50):
    print(next(pNumbers))