import abc
from ex0.Creature import Creature
from ex1.Capability import TransformCapability, HealCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(abc.ABC):

    @abc.abstractmethod
    def act(self, creature):
        pass

    @abc.abstractmethod
    def is_valid(self, creature):
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature):
        return isinstance(creature, Creature)

    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError("Battle error, aborting tournament: Invalid Creature"
            f"'{creature.name}' for this normal strategy")
        creature.attack()



class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature):
        return isinstance(creature, TransformCapability)

    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError("Battle error, aborting tournament: Invalid Creature"
            f"'{creature.name}' for this aggressive strategy")
        creature.transform()
        creature.attack()
        creature.revert()


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature):
        return isinstance(creature, HealCapability)

    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError("Battle error, aborting tournament: Invalid Creature"
            f"'{creature.name}' for this defensive strategy")
        creature.attack()
        creature.HealCapability("itself")
