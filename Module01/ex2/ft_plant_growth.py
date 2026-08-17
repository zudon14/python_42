
class Plant:
    def __init__(self, name: str, cm: float, days: int) -> None:
        self.name = name
        self.cm = cm
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {self.cm}cm, {self.days} days old")

    def grow(self) -> None:
        self.cm = round(self.cm + (self.cm / self.days), 1)

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    plant1 = Plant("Rose", 25.0, 30)
    initial_height = plant1.cm

    print("=== Garden Plant Growth ===")
    plant1.show()

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant1.grow()
        plant1.age()
        plant1.show()

    weekly_growth = plant1.cm - initial_height
    print(f"Growth this week: {weekly_growth}cm")