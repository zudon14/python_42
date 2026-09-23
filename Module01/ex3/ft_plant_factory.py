class Plant:
    def __init__(
        self, name: str, cm: float, days: int, growth_rate: float = 0.8
    ) -> None:
        self.name = name
        self.cm = cm
        self.days = days
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {self.cm}cm, {self.days} days old")

    def grow(self) -> None:
        self.cm = round(self.cm + self.growth_rate, 1)

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()
