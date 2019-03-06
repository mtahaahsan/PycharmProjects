testList1 = [1, 2, 3]
testList2 = [4, 5, 6]


# Takes two lists and iterates through them using zip to take the heads of both lists, and adds them together and
# appends them to the empty list
def seqaddi(list1, list2):
    numList = []
    for x, y in zip(list1, list2):
        numList.append(x + y)
    return numList

print(seqaddi(testList1, testList2))


# Takes two lists and iterates through them using zip to take the heads of both lists, and then multiplies them
# together and appends them to the empty list
def seqmulti(list1, list2):
    numList = []
    for x, y in zip(list1, list2):
        numList.append(x * y)
    return numList

print(seqmulti(testList1, testList2))


# Takes two lists and first checks if list1 is empty, if it is, return an empty list. Otherwise, the the lists are split
# up as the head and the rest of the list. The heads are added and put into a list, this keeps happening until the base
# case is met, once the empty list is returned, the previous lists are appended to the empty list
def seqaddr(list1, list2):
    if not list1:
        return []
    else:
        head1, *tail1 = list1
        head2, *tail2 = list2
        return [head1 + head2] + seqaddr(tail1, tail2)

print(seqaddr(testList1, testList2))


# Takes two lists and first checks if list1 is empty, if it is, return an empty list. Otherwise, the the lists are split
# up as the head and the rest of the list. The heads are multiplies and put into a list, this keeps happening until the
# base case is met, once the empty list is returned, the previous lists are appended to the empty list
def seqmultr(list1, list2):
    if not list1:
        return []
    else:
        head1, *tail1 = list1
        head2, *tail2 = list2
        return [head1 * head2] + seqmultr(tail1, tail2)

print(seqmultr(testList1, testList2))


# Takes two lists and follows a similar approach as seqaddi, but this uses list comprehension, which does the
# calculating and appending directly in the list itself
def seqaddc(list1, list2):
    return [head1 + head2 for head1, head2 in zip(list1, list2)]

print(seqaddc(testList1, testList2))


# Takes two lists and follows a similar approach as seqmulti, but this uses list comprehension, which does the
# calculating and appending directly in the list itself
def seqmultc(list1, list2):
    return [head1 * head2 for head1, head2 in zip(list1, list2)]

print(seqmultr(testList1, testList2))
