from abc import ABC, abstractmethod

from .creature import Aquabub, Creature, Flameling, Pyrodon, Torragon

class CreatureFactory(ABC):
    @abstractmethod
    def creature_base(self) -> Creature:
        raise NotImplementedError

    @abstractmethod
    def creature_evolded(self) -> Creature:
        raise NotImplementedError

class FlameFactory(CreatureFactory):
    def creature_base(self) -> Creature:
        return Flameling()

    def creature_evolded(self) -> Creature:
        return Pyrodon()

class AquaFactory(CreatureFactory):
    def creature_base(self) -> Creature:
        return Aquabub()

    def creature_evolded(self) -> Creature:
        return Torragon()