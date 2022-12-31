import zope.interface


class Interface(zope.interface.Interface):
    x=zope.interface.Attribute("I am zope interface attribute")
    def method1(self):
        pass
    def method2(self):
        pass


print(type(Interface))
print(Interface.__module__)
print(Interface.__name__)

# get attribute
x = Interface['x']
print(x)
print(type(x))