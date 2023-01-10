from abc import ABC, abstractmethod


class Browser(ABC):
    @abstractmethod
    def getBrowserDriver(self):
        pass
