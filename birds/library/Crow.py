import string

from multipledispatch import dispatch

from library.Bird import Bird


class Crow(Bird):
    def __init__(self):
        print("Crow Constructor")
    @dispatch(str)
    def fly(self,type="High"):
        print("Crow Flying "+type)
    def fly(self):
        print("Crow Flying")
    def eat(self):
        print("Crow Eating ")