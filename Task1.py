def cadd(tups, tups2):
    first, last = tups
    first2, last2 = tups2
    return ((first + first2), (last + last2))


print(cadd((1, 23), (4, 1)))

def cmult(tups, tups2):
    first, second = tups
    first2, second2 = tups2
    return ((first*first2), (second*second2))

print(cmult((1,2), (12,124)))

