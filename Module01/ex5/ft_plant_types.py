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
        self._height = round(
            self._height + 2.35, 1
        )

    def age(self) -> None:
        self._age += 1


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color = color

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height}cm long and "
            f"{self.trunk_diameter}cm wide."
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1


if __name__ == "__main__":
    flower1 = Flower("Rose", 15.0, 10, "red")
    tree1 = Tree("Oak", 200.0, 365, 5.0)
    vegetable1 = Vegetable("Tomato", 5.0, 10, "April")

    print("=== Garden Plant Types ===")

    print("=== Flower")
    flower1.show()
    print("Rose has not bloomed yet")
    print("[asking the rose to bloom]")
    flower1.show()
    flower1.bloom()

    print("=== Tree")
    tree1.show()
    print("[asking the oak to produce shade]")
    tree1.produce_shade()

    print("=== Vegetable")
    vegetable1.show()
    print("[make tomato grow and age for 20 days]")

    for i in range(20):
        vegetable1.grow()
        vegetable1.age()

    vegetable1.show()