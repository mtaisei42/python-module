import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._rank_count = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def _store(self, values: list[str]) -> None:
        for value in values:
            self._storage.append((self._rank_count, value))
            self._rank_count += 1

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No processed data available")
        return self._storage.pop(0)

    def get_total(self) -> int:
        return self._rank_count

    def get_remaining(self) -> int:
        return len(self._storage)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        return isinstance(data, (int, float)) or (
            isinstance(data, list)
            and all(isinstance(value, (int, float)) for value in data)
        )

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        values = data if isinstance(data, list) else [data]
        self._store([str(value) for value in values])


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        return isinstance(data, str) or (
            isinstance(data, list)
            and all(isinstance(value, str) for value in data)
        )

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        values = data if isinstance(data, list) else [data]
        self._store(values)


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        values = data if isinstance(data, list) else [data]
        return all(
            isinstance(value, dict)
            and all(isinstance(key, str) for key in value)
            and all(isinstance(item, str) for item in value.values())
            for value in values
        )

    def ingest(
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        values = data if isinstance(data, list) else [data]
        messages: list[str] = []
        for value in values:
            if "log_level" in value and "log_message" in value:
                messages.append(
                    f"{value['log_level']}: {value['log_message']}"
                )
            else:
                messages.append(
                    ", ".join(f"{key}: {item}" for key, item in value.items())
                )
        self._store(messages)


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            for proc in self.processors:
                if proc.validate(element):
                    try:
                        proc.ingest(element)
                    except (TypeError, ValueError) as error:
                        print(f"DataStream error - {error}")
                    break
            else:
                print("DataStream error - Can't process element in stream: "
                      f"{element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(f"{name}: total {proc.get_total()} items processed, "
                  f"remaining {proc.get_remaining()} on processor")


def main() -> None:
    stream = DataStream()
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    stream.print_processors_stats()
    print("\nRegistering Numeric Processor")
    stream.register_processor(numeric)
    data: list[typing.Any] = [
        "Hello world", [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42, ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {data}")
    stream.process_stream(data)
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    stream.register_processor(text)
    stream.register_processor(log)
    print("Send the same batch again")
    stream.process_stream(data)
    stream.print_processors_stats()

    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    log.output()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
