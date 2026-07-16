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

    def get_total(self) -> int:
        return self._rank_count

    def get_remaining(self) -> int:
        return (len(self._storage))


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
            self._storage.append((self._rank_count, str(data)))
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

class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    break
            else:
                print(f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not len(self.processors):
            print("No processor found, no data")
            return

        for proc in self.processors:
            print(f"{proc.__class__.__name__}:"
                  f"total {proc.get_total()} item processed, "
                  f"remaining {proc.get_remaining()} on processor")

def main() -> None:
    stream = DataStream()
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()


    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    stream.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    stream.register_processor(numeric)
    data = ['Hello world', [3.14, -1, 2.71],
            [{'log_level': 'WARNING','log_message': 'Telnet access! Use ssh instead'},
             {'log_level': 'INFO','log_message': 'User wil isconnected'}],
             42, ['Hi','five']]
    print(f"Send first batch of data on stream: {data}")
    stream.process_stream(data)

    stream.print_processors_stats()
    print("\nRegistering other data processors")
    stream.register_processor(text)
    stream.register_processor(log)
    print("Send the same batch again")
    stream.process_stream(data)
    stream.print_processors_stats()
    print("\nConsume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    log.output()
    stream.print_processors_stats()



main()
