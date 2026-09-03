import abc
from ex1 import Capability, Creature


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
        return isinstance(creature, Creature.Creature)

    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError()
        creature.attack()



class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature):
        return isinstance(creature, Capability.TransformCapability)

    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError
        creature.transform()
        creature.attack()
        creature.revert()


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature):
        return isinstance(creature, Capability.HealCapability)

    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError
        creature.attack()
        creature.HealCapability("itself")
