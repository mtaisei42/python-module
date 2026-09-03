import abc
from .Creature import Aquabub, Torragon, Flameling, Pyrodon


class CreatureFactory(abc.ABC):

    @abc.abstractmethod
    def create_base(self):
        pass

    @abc.abstractmethod
    def create_evolved(self):
        pass


class AquaFactory(CreatureFactory):

    def create_base(slf):
        return Aquabub()


    def create_evolved(slf):
        return Torragon()


class FlameFactory(CreatureFactory):

    def create_base(slf):
        return Flameling()


    def create_evolved(slf):
        return Pyrodon()
