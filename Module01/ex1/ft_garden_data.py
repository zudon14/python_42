
class Plant:
    def __init__(self, name: str, cm: float, days: int) -> None:
        self.name = name
        self.cm = cm
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {self.cm}cm, {self.days} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()
