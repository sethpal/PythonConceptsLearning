from multipledispatch import dispatch

from library.Animal import Animal


class Bird:
    def __init__(self):
        print("Bird Constructor")


    def fly(self):
        print("Some Bird fly some do not fly")