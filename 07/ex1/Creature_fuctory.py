import abc
from .Creature import Aquabub, Torragon, Flameling, Pyrodon
from .Creature import Sproutling, Bloomelle, Shiftling, Morphagon


class CreatureFactory(abc.ABC):

    @abc.abstractmethod
    def create_base(self):
        pass

    @abc.abstractmethod
    def create_evolved(self):
        pass


class HeelingCreatureFactory(CreatureFactory):

    def create_base(self):
        return Sproutling()

    def create_evolved(self):
        return Bloomelle()

class TransformCreatureFactory(CreatureFactory):

    def create_base(self):
        return Shiftling()

    def create_evolved(self):
        return Morphagon()
