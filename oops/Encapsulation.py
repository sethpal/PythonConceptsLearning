# Python program to
# demonstrate protected members

# Creating a base class
class Base:
    def __init__(self):
        # Protected member defined with single underscore
        self._a = 2
        # Private members are defined with double underscore, outside class not accessible
        self.__c = "GeeksforGeeks"
        self._d = "GeeksforGeeks"
    def __del__(self):
        print("Destructor is called Now for Class Name:", self.__class__.__name__)

# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ",
              self._a, self._d)
        #private mambers are accessible outside class , even in child class,hence commented below line
        #print(self.__c)

        # Modify the protected variable:
        self._a = 3
        print("Calling modified protected member outside class: ",
              self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)