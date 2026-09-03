import abc
import typing
from .Capability import HealCapability, TransformCapability

class Creature(abc.ABC):

    def __init__(self, name, type):
        self.name = name
        self.type = type

    @abc.abstractmethod
    def attack(self):
        pass


    def describe(self):
        print(f"{self.name} is a {self.type} type Creature")


class Sproutling(Creature, HealCapability):

    def __init__(self):
        super().__init__("Sproutling", "Water")

    def attack(self):
        print(f"{self.name} uses Vine Whip!")

    def HealCapability(self, target):
        print(f"{self.name} heals {target} for a small amount")


class Bloomelle(Creature, HealCapability):

    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self):
        print(f"{self.name} uses Petal Dance!")

    def HealCapability(self, target):
        print(f"{self.name} heals {target} for a large amount")


class Shiftling(Creature, TransformCapability):

    def __init__(self):
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)
    def attack(self):
        if not self.is_transformed:
            print(f"{self.name} attacks normally.")
        else:
            print(f"{self.name} performs a boosted strike!")

    def transform(self):
        self.is_transformed = True
        print(f"{self.name} shifts into a sharper form!")


    def revert(self):
        self.is_transformed = False
        print(f"{self.name} returns to normal.")


class Morphagon(Creature, TransformCapability):

    def __init__(self):
        Creature.__init__(self, "Morphagon", "Nomal/Dragon")
        TransformCapability.__init__(self)

    def attack(self):
        if not self.is_transformed:
            print(f"{self.name} attacks normally")
        else:
            print(f"{self.name} unleashes a devastating morph strike!")

    def transform(self):
        self.is_transformed = True
        print(f"{self.name} morphs into a dragonic battle form!")

    def revert(self):
        self.is_transformed = False
        print(f"{self.name} stabilizes its form.")
