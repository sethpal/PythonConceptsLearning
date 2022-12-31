from abc import ABC, abstractmethod, abstractproperty


class Shape(ABC):
    def __init__(self,shape_name):
        self.shape_name= shape_name
    @abstractmethod
    def draw(self):
        pass
    @abstractproperty
    def  name(self):
        pass