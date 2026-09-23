from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type_: str) -> None:
        self.name = name
        self.type_ = type_

    @abstractmethod
    def attack(self) -> str:
        """Each specific creature defines its own attack."""
        raise NotImplementedError

    def describe(self) -> str:
        return f"{self.name} is a {self.type_} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__(name="Flameling", type_="Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Pyrodon", type_="Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__(name="Aquabub", type_="Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Torragon", type_="Water")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
