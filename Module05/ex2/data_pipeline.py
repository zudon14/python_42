import abc
from typing import Any, Protocol


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
            and all(isinstance(item, (int, float)) for item in data)
        )

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self.itens.append(str(item))
        else:
            self.itens.append(str(data))


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) or (
            isinstance(data, list)
            and all(isinstance(item, str) for item in data)
        )

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            self.itens.extend(data)
        else:
            self.itens.append(data)


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self._is_valid_log(data)

        if isinstance(data, list):
            return all(
                isinstance(item, dict) and self._is_valid_log(item)
                for item in data
            )

        return False

    @staticmethod
    def _is_valid_log(log: dict[Any, Any]) -> bool:
        return (
            all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in log.items()
            )
            and "log_level" in log
            and "log_message" in log
        )

    def ingest(
        self,
        data: dict[str, str] | list[dict[str, str]],
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        logs = data if isinstance(data, list) else [data]
        for log in logs:
            entry = log["log_level"] + ": " + log["log_message"]
            self.itens.append(entry)


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _, value in data]
        csv_str = ",".join(values)
        print("CSV Output:")
        print(csv_str)


class JSONPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pairs = [f'"item_{rank}": "{value}"' for rank, value in data]
        json_str = "{" + ", ".join(pairs) + "}"
        print("JSON Output:")
        print(json_str)


class DataStream:

    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            processed = False

            for processor in self.processors:
                if processor.validate(data):
                    processor.ingest(data)
                    processed = True
                    break

            if not processed:
                print(
                    "DataStream error - Can't process element "
                    f"in stream: {data}"
                )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            collected: list[tuple[int, str]] = []

            for _ in range(nb):
                try:
                    collected.append(processor.output())
                except IndexError:
                    break

            if collected:
                plugin.process_output(collected)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self.processors:
            print("No processor found, no data")
            return

        for processor in self.processors:
            total = processor.rank + len(processor.itens)
            remaining = len(processor.itens)
            name = processor.__class__.__name__.replace(
                "Processor", " Processor"
            )
            print(
                f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...\n")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors\n")
    numeric_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(numeric_proc)
    stream.register_processor(text_proc)
    stream.register_processor(log_proc)

    batch_1: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch_1}\n")
    stream.process_stream(batch_1)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVPlugin())
    stream.print_processors_stats()

    batch_2: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"\nSend another batch of data: {batch_2}\n")
    stream.process_stream(batch_2)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONPlugin())
    stream.print_processors_stats()