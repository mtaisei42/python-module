import abc
import typing


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class JsonPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        json_data: list[str] = []
        for rank, value in data:
            json_data.append(f'"item_{rank}": "{value}"')
        print("Json Output:")
        print("{" + ", ".join(json_data) + "}")


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        csv_data: list[str] = []
        for value in data:
            csv_data.append(value[1])
        print("CSV Output:")
        print(",".join(csv_data))



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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            output_data: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    output_data.append(proc.output())
                except IndexError:
                    break
            if output_data:
                plugin.process_output(output_data)

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

    print("=== Code Nexus - Data Pipeline ===")
    print("\nInitialize Data Stream...\n")
    stream.print_processors_stats()
    print("\nRegistering Processors\n")
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    data = ['Hello world', [3.14, -1, 2.71],
            [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
             {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
             42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {data}\n")
    stream.process_stream(data)
    stream.print_processors_stats()
    print()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVPlugin())
    print()
    stream.print_processors_stats()
    print()
    data = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
            [{'log_level': 'ERROR', 'log_message': '500 server crash'},
             {'log_level': 'NOTICE', 'log_message': 'Certificateexpires in 10 days'}],
             [32, 42, 64, 84, 128, 168], 'World hello']

    print(f"Send another batch of data: {data}\n")
    stream.process_stream(data)

    stream.print_processors_stats()
    print()
    print("Send 5 processed data form each processor to a JSON plugin:")
    stream.output_pipeline(5, JsonPlugin())
    print()
    stream.print_processors_stats()


main()
