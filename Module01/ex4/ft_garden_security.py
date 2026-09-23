class Plant:
    def __init__(
        self, name: str, height: float, age: int, growth_rate: float = 0.8
    ) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self._growth_rate = growth_rate
        # Invalid values are rejected: the plant keeps the defaults above.
        self.set_height(height)
        self.set_age(age)

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def grow(self, amount: float | None = None) -> None:
        if amount is None:
            amount = self._growth_rate
        self._height = round(self._height + amount, 1)

    def age(self, days: int = 1) -> None:
        self._age += days

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return False
        self._height = height
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            return False
        self._age = age
        return True


if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose.show()
    print()

    if rose.set_height(25.0):
        print(f"Height updated: {rose.get_height():.0f}cm")
    if rose.set_age(30):
        print(f"Age updated: {rose.get_age()} days")
    print()

    if not rose.set_height(-5):
        print("Height update rejected")
    if not rose.set_age(-10):
        print("Age update rejected")
    print()

    print("Current state: ", end="")
    rose.show()
