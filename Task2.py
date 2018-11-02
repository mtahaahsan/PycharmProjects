list1 = [1,2,3]
list2 = [4,5,6]
list = []


def seqaddi(list1, list2):
        for x in zip(list1, list2):
            list.append(sum(x))
        return list

def seqmulti (list1, list2):
    for x,y in zip(list1, list2):
        z=x*y
        list.append(z)
    return list

def seqaddr(list1, list2):
    if not list1:
        first,*rest = list1
        first2,*rest2 = list2
    list.append(first+first2)
    seqaddr(rest, rest2)
    return list


print(seqaddr(list1,list2))

