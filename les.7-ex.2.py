from abc import ABC, abstractmethod


class Clother(ABC):

    def __init__(self, p):
        self.p = p

    @abstractmethod
    def cloth(self):
        result = 0


class Coat(Clother):

    @property
    def cloth(self):
        result = self.p / 6.5 + 0.5
        return result


class Costum(Clother):

    @property
    def cloth(self):
        result = 2 * self.p + 0.3
        return result


one = Coat(cdc)
print(one.cloth)
