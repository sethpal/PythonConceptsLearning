from multipledispatch import dispatch

from library.Bird import Bird
from library.Crow import Crow


class Pigeon(Crow):
    def __init__(self):
        super().__init__()
        print("Pigeon constructor")
    def fly1(self):
        # this will print only grand parent Bird result
        Bird.fly(self)
        #this will print super class method
        #super().fly()

    def eat(self):
        print("Eat once")
    @dispatch(int)
    def eat(self, time):
        print("Eat time"+time)