
class Plant:
    def __init__(self, name: str, cm: float, days: int) -> None:
        self.name = name
        self.cm = cm
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {self.cm}cm, {self.days} days old")

    def grow(self) -> None:
        if self.cm == 0:
            return
        self._height = round(self.cm + (self.cm / self.days), 1)

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    plant1 = Plant("Rose", 25.0, 30)
    plant2 = Plant("Oak", 200.0, 365)
    plant3 = Plant("Cactus", 5.0, 90)
    plant4 = Plant("Sunflower", 80.0, 45)
    plant5 = Plant("Fern", 15.0, 120)

    print("=== Plant Factory Output ===")

    print("Created: ", end="")
    plant1.show()

    print("Created: ", end="")
    plant2.show()

    print("Created: ", end="")
    plant3.show()

    print("Created: ", end="")
    plant4.show()

    print("Created: ", end="")
    plant5.show()
