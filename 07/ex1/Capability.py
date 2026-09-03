import abc
import typing


class HealCapability(abc.ABC):

    @abc.abstractmethod
    def HealCapability(self, target):
        pass



class TransformCapability(abc.ABC):

    def __init__(self):
        self.is_transformed = False


    @abc.abstractmethod
    def transform(self):
        pass


    @abc.abstractmethod
    def revert(self):
        pass
