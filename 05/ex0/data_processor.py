import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self):
        self._storage: list[tuple[int, str]] = []
        self._rank_count: int = 0
    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int,str]:
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):

    def validate(self, data :typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if (isinstance(data, list)
            and len(data) > 0
            and all(isinstance(x, (int, float)) for x in data)):
            return True
        return False

    def ingest(self, data :int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, (int, float)):
            self._storage.append(self._rank_count, str(data))
            self._rank_count += 1
        else:
            for value in data:
                self._storage.append((self._rank_count, str(value)))
                self._rank_count += 1


class TextProcessor(DataProcessor):

    def validate(self, data :typing.Any) -> bool:
        if isinstance(data ,str):
            return True
        if (isinstance(data, list)
            and len(data) > 0
            and all(isinstance(value, str) for value in data)):
            return True
        return False

    def ingest(self, data :str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper test data")
        if isinstance(data, str):
            self._storage.append((self._rank_count, data))
            self._rank_count += 1
        else:
            for value in data:
                self._storage.append((self._rank_count, value))
                self._rank_count += 1


class LogProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if (isinstance(data, dict)
            and len(data) > 0
            and all(isinstance(key, str) for key in data)
            and all(isinstance(val, str) for val in data.values())):
            return True
        if (isinstance(data, list)
            and len(data) > 0
            and all(isinstance(d, dict) for d in data)):
            for d in data:
                if (len(d) == 0 or
                    not(all(isinstance(key, str) for key in d)
                    and all(isinstance(val, str)for val in d.values()))):
                    return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, dict):
            log_str = f"{data['log_level']}: {data['log_message']}"
            self._storage.append((self._rank_count, log_str))
            self._rank_count += 1
        else:
            for d in data:
                log_str = f"{d['log_level']}: {d['log_message']}"
                self._storage.append((self._rank_count, log_str))
                self._rank_count += 1


def main() -> None:
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    print(f" Trying to validate input '42': "
          f"{numeric.validate(42)}")
    print(f" Trying to balidate input 'Hello'"
          f"{numeric.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")

    print(" Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, val = numeric.output()
        print(f" Numeric value {rank}: {val}")

    print("\nTesting Text Processor...")
    print(" Trying to validate input '42': "
          f"{text.validate(42)}")
    print(" Processing data: ['Hello', 'Nuxus', 'World']")
    text.ingest(['Hello', 'Nuxus', 'World'])
    print(" Extracting 1 value...")
    rank, val = text.output()
    print(f" Text value {rank}: {val}\n")

    print("Testing Log Processor...")
    print(" Trying to validate input 'Hello'"
          f"{log.validate('Hello')}")
    print(" Processing data: [{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, "
          "{'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]")
    log.ingest([
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ])

    print(" Extracting 2 values...")
    for _ in range(2):
        rank, val = log.output()
        print(f" Log entry {rank}: {val}")

main()
