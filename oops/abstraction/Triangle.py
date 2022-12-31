from oops.abstraction.Shape import Shape


class Triangle(Shape):
    def __init__(self):
        super().__init__("Triangle")
    def draw(self):
        print("Drawing Triangle")

    @property
    def name(self):
        return self.shape_name