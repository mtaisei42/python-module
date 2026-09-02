import abc
import typing


class Creature(abc.ABC):

    def __init__(self, name, type):
        self.name = name
        self.type = type

    @abc.abstractmethod
    def attack(self):
        pass


    def describe(self):
        print(f"{self.name} is a {self.type} type Creature")


class CreatureFactory(abc.ABC):

    @abc.abstractmethod
    def create_base(self):
        pass

    @abc.abstractmethod
    def create_evolved(self):
        pass

class Flameling(Creature):

    def attack(self):
        print(f"{self.name} uses {self.type}")




class Pyrodon(Creature):

    def attack(self):
        print(f"{self.name} uses {self.type}")


class Aquabub(Creature):

    def attack(self):
        print(f"{self.name} uses {self.type}")

class TTorragon(Creature):

    def attack(self):
        print(f"{self.name} uses {self.type}")


class
