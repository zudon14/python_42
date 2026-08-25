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
    def ingest(self, data: Any) -> None:
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

    def ingest(self, data: Any) -> None:
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

    def ingest(self, data: Any) -> None:
        if isinstance(data, str):
            self.itens.append(data)

        elif isinstance(data, list):
            if not all(
                isinstance(item, str)
                for item in data
            ):
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


class DataStream:

    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(
        self,
        proc: DataProcessor
    ) -> None:
        self.processors.append(proc)

    def process_stream(
        self,
        stream: list[Any]
    ) -> None:
        for data in stream:
            processed = False

            for processor in self.processors:
                if processor.validate(data):
                    processor.ingest(data)
                    processed = True
                    break

            if not processed:
                print(
                    "DataStream error - Can't process "
                    "element in stream:",
                    data
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self.processors:
            print("No processor found, no data")
            return

        for processor in self.processors:
            total = processor.rank + len(processor.itens)
            remaining = len(processor.itens)

            processor_name = processor.__class__.__name__

            print(
                processor_name.replace(
                    "Processor",
                    " Processor"
                )
                + ": total "
                + str(total)
                + " items processed, remaining "
                + str(remaining)
                + " on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")

    stream = DataStream()

    stream.print_processors_stats()

    print("Registering Numeric Processor")

    numeric = NumericProcessor()

    stream.register_processor(numeric)

    data = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected"
            }
        ],
        42,
        ["Hi", "five"]
    ]

    print("Send first batch of data on stream:", data)

    stream.process_stream(data)

    stream.print_processors_stats()

    print("Registering other data processors")

    text = TextProcessor()
    log = LogProcessor()

    stream.register_processor(text)
    stream.register_processor(log)

    print("Send the same batch again")

    stream.process_stream(data)

    stream.print_processors_stats()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    for _ in range(3):
        numeric.output()

    for _ in range(2):
        text.output()

    for _ in range(1):
        log.output()

    stream.print_processors_stats()


if __name__ == "__main__":
    main()