print("I love you")
print(["ABC", "It's as easy as", "1 2 3"][1][2:-3])
list1 = [[],[]]
tupe1 = (5)
tupe2 = (5)
print(tupe1 == tupe2) 

def f (x): return x+1;

def life(l, someList):
    for x in range(len(someList)):
        someList[x] = f(someList[x])
    return someList

print(life(lambda x:x+1, [1,2,3,4]))