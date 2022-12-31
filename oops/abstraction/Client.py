from oops.abstraction.Circle import Circle
from oops.abstraction.Triangle import Triangle

objs=[Circle("Circle"),Triangle()]

for ob in objs:
    ob.draw()
    print(ob.name)