myList = ["eat", "sleep", "code"]

# Uses the concept of generators to return the different strings, we use yield and generators can keep track of where
# the loop last stopped by using yield, this allows us to create an endless cycle
def cycleoflife():
    while True:
        yield myList[0]
        yield myList[1]
        yield myList[2]

x = cycleoflife();

for i in range(0, 7000):
    print(next(x))
