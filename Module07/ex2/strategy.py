from abc import ABC, abstractmethod

from ex0.creature import Creature
from ex1.heal_capability import HealCapability
from ex1.transform_capability import TransformCapability

class InvalidStrategyError(Exception):
    """Raised when a strategy is applied to an incompatible Creature."""

class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        raise NotImplementedError

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        raise NotImplementedError

class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        return [creature.attack()]

class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this aggressive strategy"
            )
        assert isinstance(creature, TransformCapability)
        return [creature.transform(), creature.attack(), creature.revert()]

class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this defensive strategy"
            )
        assert isinstance(creature, HealCapability)
        return [creature.attack(), creature.heal()]
