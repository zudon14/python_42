from ex0.factory import CreatureFactory
from ex0.factory import Creature

from .creature import Bloomelle, Morphagon, Shiftling, Sproutling

class HealingCreatureFactory(CreatureFactory):
    def creature_base(self) -> Creature:
        return Sproutling()

    def creature_evolded(self) -> Creature:
        return Bloomelle()

class TransformCreatureFactory(CreatureFactory):
    def creature_base(self) -> Creature:
        return Shiftling()

    def creature_evolded(self) -> Creature:
        return Morphagon()
    