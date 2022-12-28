class Addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second

def swap(x, y):
        temp = x
        x = y
        y = temp
        return x,y

cube=lambda x:x*x*x
square= lambda x:x*x


print(cube(300000000000000000000000000000000000000))
# Driver code
x = 2
y = 3
x,y=swap(x, y)
print(x)
print(y)
# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(1000, 2000)

# creating second object of same class
obj2 = Addition(10, 20)

list=[obj1,obj2]

for ob in list:
    ob.calculate()
    ob.display()
