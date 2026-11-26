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


def main() -> None:
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        # Deliberate mypy warning for the required invalid-input test.
        numeric.ingest("foo")
    except ValueError as error:
        print(f"Got exception: {error}")
    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f"Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    print(f"Trying to validate input '42': {text.validate(42)}")
    print(f"Trying to validate input 'Hello': {text.validate('Hello')}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    rank, value = text.output()
    print(f"Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Trying to validate log input: {log.validate(logs)}")
    print(f"Processing data: {logs}")
    log.ingest(logs)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
