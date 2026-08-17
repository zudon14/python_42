class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self) -> None:
        if self._age == 0:
            return
        self._height = round(self._height + (self._height / self._age), 1)

    def age(self) -> None:
        self._age += 1

    def set_height(self, height: float) -> None:
        if height < 0:
            print("Rose: Error, height can't be negative")
            return
        self._height = height

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print("Rose: Error, age can't be negative")
            return
        self._age = age

    def get_age(self) -> int:
        return self._age


if __name__ == "__main__":
    plant1 = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    plant1.show()

    plant1.set_height(25.0)
    print("Height updated: 25cm")

    plant1.set_age(30)
    print("Age updated: 30 days")

    plant1.set_height(-5)
    print("Height update rejected")

    plant1.set_age(-10)
    print("Age update rejected")

    print("Current state: ", end="")
    plant1.show()