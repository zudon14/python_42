import abc
from typing import Any


class DataProcessor(abc.ABC):

    def __init__(self) -> None:
        super().__init__()
        self.itens: list[str] = []
        self.rank: int = 0

    @abc.abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abc.abstractmethod
    def ingest(self, data: int | float | list[int | float]) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if not self.itens:
            raise IndexError("No data available")

        item = self.itens.pop(0)
        result = (self.rank, item)
        self.rank += 1

        return result


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        return isinstance(data, (int, float)) or (
            isinstance(data, list)
            and all(
                isinstance(item, (int, float))
                for item in data
            )
        )

    def ingest(self, data: str | list[str]) -> None:
        if isinstance(data, (int, float)):
            self.itens.append(str(data))

        elif isinstance(data, list):
            if not all(
                isinstance(item, (int, float))
                for item in data
            ):
                raise ValueError("Improper numeric data")

            for item in data:
                self.itens.append(str(item))

        else:
            raise ValueError("Improper numeric data")


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) or (
            isinstance(data, list)
            and all(isinstance(item, str) for item in data)
        )

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if isinstance(data, str):
            self.itens.append(data)

        elif isinstance(data, list):
            if not all(isinstance(item, str) for item in data):
                raise ValueError("Improper text data")

            for item in data:
                self.itens.append(item)

        else:
            raise ValueError("Improper text data")


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return (
                all(
                    isinstance(key, str)
                    and isinstance(value, str)
                    for key, value in data.items()
                )
                and "log_level" in data
                and "log_message" in data
            )

        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(
                    isinstance(key, str)
                    and isinstance(value, str)
                    for key, value in item.items()
                )
                and "log_level" in item
                and "log_message" in item
                for item in data
            )

        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, dict):
            item = (
                data["log_level"]
                + ": "
                + data["log_message"]
            )
            self.itens.append(item)

        elif isinstance(data, list):
            for log in data:
                item = (
                    log["log_level"]
                    + ": "
                    + log["log_message"]
                )
                self.itens.append(item)


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Testing Numeric Processor...")
    print(
        "Trying to validate input '42':",
        numeric.validate(42)
    )
    print(
        "Trying to validate input 'Hello':",
        numeric.validate("Hello")
    )

    print(
        "Test invalid ingestion of string 'foo' "
        "without prior validation:"
    )

    try:
        numeric.ingest("foo")
    except ValueError as error:
        print("Got exception:", error)

    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])

    print("Extracting 3 values...")

    for _ in range(3):
        rank, value = numeric.output()
        print("Numeric value", rank, ":", value)

    print("Testing Text Processor...")

    print(
        "Trying to validate input '42':",
        text.validate(42)
    )

    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(["Hello", "Nexus", "World"])

    print("Extracting 1 value...")

    rank, value = text.output()
    print("Text value", rank, ":", value)

    print("Testing Log Processor...")

    print(
        "Trying to validate input 'Hello':",
        log.validate("Hello")
    )

    logs = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server"
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!"
        }
    ]

    print("Processing data:", logs)
    log.ingest(logs)

    print("Extracting 2 values...")

    for _ in range(2):
        rank, value = log.output()
        print("Log entry", rank, ":", value)


if __name__ == "__main__":
    main()