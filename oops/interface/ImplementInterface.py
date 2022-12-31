import zope.interface

from oops.interface.Interface import Interface


@zope.interface.implementer(Interface)
class ImplInterface():
    def method1(self,x):
        return x**2

    def method2(self):
        return "I am in Method2"