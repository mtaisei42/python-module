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


class Flameling(Creature):

    def __init__(self):
        super().__init__("Flameling", "fire")

    def attack(self):
        print(f"{self.name} uses Ember!")


class Pyrodon(Creature):

    def __init__(self):
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self):
        print(f"{self.name} uses Flamethrower!")


class Aquabub(Creature):

    def __init__(self):
        super().__init__("Aquabub", "Water")


    def attack(self):
        print(f"{self.name} uses Water Gum!")


class Torragon(Creature):

    def __init__(self):
        super().__init__("Torragon", "Water")

    def attack(self):
        print(f"{self.name} uses Hydro Pump!")
