from oops.abstraction.Shape import Shape


class Circle(Shape):
    def __init__(self,shape_name):
        self.shape_name=shape_name
    def draw(self):
        print("Drawing ",self.shape_name)
    @property
    def name(self):
        return self.shape_name