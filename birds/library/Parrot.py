from multipledispatch import dispatch

from library.Bird import Bird


class Parrot(Bird):
    def __init__(self):
        print("Parrot constructor")

    @dispatch()
    def fly(self):
        print("Parrot can fly")