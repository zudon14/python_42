
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

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        if age > 365:
            return 1
        return 0
    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)