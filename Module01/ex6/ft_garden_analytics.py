class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age
        self._stats = self.Stats()

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")
        self._stats.increment_show()

    def grow(self) -> None:
        if self._age == 0:
            return
        self._height = round(self._height + 0.8, 1)
        self._stats.increment_grow()

    def age(self) -> None:
        self._age += 1
        self._stats.increment_age()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def increment_grow(self) -> None:
            self._grow_count += 1

        def increment_age(self) -> None:
            self._age_count += 1

        def increment_show(self) -> None:
            self._show_count += 1

        def stats_show(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, "
                f"{self._show_count} show"
            )


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


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self.seed_count = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seed_count}")

    def bloom(self) -> None:
        super().bloom()
        self.seed_count = 42


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._shade_count = 0

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height}cm long and "
            f"{self.trunk_diameter}cm wide."
        )
        self._shade_count += 1


def show_statistics(plant: Plant) -> None:
    plant._stats.stats_show()

    if isinstance(plant, Tree):
        print(f"{plant._shade_count} shade")


if __name__ == "__main__":
    flower1 = Flower("Rose", 15.0, 10, "red")
    tree1 = Tree("Oak", 200.0, 365, 5.0)
    seed1 = Seed("Sunflower", 80.0, 45, "yellow")
    anonymous = Plant.create_anonymous()

    print("=== Garden Analytics ===")

    print("=== Check year-old ===")
    print(
        f"Is 30 days more than a year? "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        f"Is 400 days more than a year? "
        f"{Plant.is_older_than_year(400)}"
    )

    print("=== Flower")
    flower1.show()
    print("Rose has not bloomed yet")
    print("[statistics for Rose]")
    show_statistics(flower1)

    print("[asking the rose to grow and bloom]")
    flower1.grow()
    flower1.bloom()
    flower1.show()
    print("[statistics for Rose]")
    show_statistics(flower1)

    print("=== Tree")
    tree1.show()
    print("[statistics for Oak]")
    show_statistics(tree1)

    print("[asking the oak to produce shade]")
    tree1.produce_shade()
    print("[statistics for Oak]")
    show_statistics(tree1)

    print("=== Seed")
    seed1.show()
    print("Sunflower has not bloomed yet")
    print("[make sunflower grow, age and bloom]")
    seed1.grow()
    seed1.age()
    seed1.bloom()
    seed1.show()
    print("[statistics for Sunflower]")
    show_statistics(seed1)

    print("=== Anonymous")
    anonymous.show()
    print("[statistics for Unknown plant]")
    show_statistics(anonymous)
