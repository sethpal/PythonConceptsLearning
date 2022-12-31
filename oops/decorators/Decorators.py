#Decorators are a very powerful and useful tool in Python since it allows programmers
# to modify the behaviour of a function or class. Decorators allow us to wrap another
# function in order to extend the behaviour of the wrapped function, without permanently
# modifying it. But before diving deep into decorators let us understand some concepts that
# will come in handy in learning the decorators.


class Decorator():
    def __init__(self):
        print("In Decorator")

    def shout(self,text):
        return text.upper()

    def small(self,text):
        return text.lower()

    def greet(self,func,text):
        greeting=func(text)
        print(greeting)

ob=Decorator()
string: str="Hi, I am created by a function passed as an argument."
ob.greet(ob.shout, string)
ob.greet(ob.small, string)