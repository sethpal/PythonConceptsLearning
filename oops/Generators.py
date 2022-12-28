def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)


# A generator function
def simpleGeneratorFun():
    yield 4
    yield 5
    yield 6


# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next
while(x):
    try:
        print(x.__next__())
    except:
        #print("Exception ")
        break;