# Takes in an integer, if the integer is 0, it returns an empty list, otherwise, it recursively calls itself until it
# reaches the base case, for each iteration, an empty list is returned and then put inside a list from the previous call
def fenc(x):
    if(x == 0):
        return []
    else:
        return [fenc(x-1), [fenc(x-1)]]

print(fenc(2))


# Takes in a list and checks to see if the list is empty, if not, then the method is recursively called and the head of
# of the list is passed in. The '1' is added to keep track of how many lists were iterated before an empty list was
# found
def fdec(listdenc):
    if not listdenc:
        return 0
    else:
        return 1+fdec(listdenc[0])

test = fenc(2)
print(fdec(test))