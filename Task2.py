list1 = [1, 2, 3]
list2 = [4, 5, 6]
numlist = []


def seqaddi(list1, list2):
    numlist = []
    for x, y in zip(list1, list2):
        numlist.append(x+y)
    return numlist


def seqmulti(list1, list2):
    numlist = []
    for x, y in zip(list1, list2):
        z = x * y
        numlist.append(z)
    return numlist


def seqaddr(list1, list2):
    if not list1:
        print(numlist)
    else:
        first, *rest = list1
        first2, *rest2 = list2
        numlist.append(first + first2)
        seqaddr(rest, rest2)

def seqmultr(list1, list2):
    if not list1:
        print(numlist)
    else:
        first , *rest = list1
        first2, *rest2 = list2
        numlist.append(first*first2)
        seqmultr(rest, rest2)

def seqaddc(list1, list2):
    lst = [x+y for x,y in zip(list1, list2)]
    print(lst)

def seqmultc(list1, list2):
    lst = [x*y for x,y in zip(list1, list2)]
    print(lst)


seqmultc(list1, list2)

print(seqaddi(list1, list2))



