from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self,shape_name):
        self.shape_name= shape_name
    @abstractmethod
    def draw(self):
        pass
