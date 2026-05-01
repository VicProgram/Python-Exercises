from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[str] = []
        self.count = 0

    @abstractmethod
    def validate(self, data: Any) -> bool: pass

    @abstractmethod
    def ingest(self, data: Any) -> None: pass

    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise IndexError("No data to process")
        item = self.storage.pop(0)
        rank = self.count
        return (rank, item)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return (True)
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:

        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self.storage.append(str(item))
                self.count += 1
        else:
            self.storage.append(str(data))
        self.count += 1

class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:

        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, str):
            data = [data]
        if isinstance(data, list):
            for x in data:
                self.storage.append(x)
                self.count += 1
        self.count += 1

class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return True
        if isinstance(data, list):
            return all(isinstance(x, dict) for x in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
            
        items = data if isinstance(data, list) else [data]
        for item in items:
            item_entry = ": ".join(str(v) for v in item.values())
            self.storage.append(item_entry)
            self.count += 1
        
class DataStream:

    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            processed = False
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    processed = True
                    break
            if not processed:
                print(
                    f"DataStream error - Can't process"
                    f" element in stream: {item}"
                )

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processor found, no data")
            return
        print("== DataStream statistics ==")
        for proc in self.processors:
            name = type(proc).__name__
            total = proc.count
            remaining = len(proc.storage)
            print(
                f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print("\n Initialize Data Stream...")
    print()

    ds = DataStream()
    ds.print_processors_stats()

    print("\n Registering Numeric Processor")

    ds.register_processor(NumericProcessor())

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [{
            'log_level': 'WARNING',
            'log_message': 'Telnet access! Use ssh instead'
          },
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]

    print("Send first batch of data on stream:")

    ds.process_stream(batch)
    ds.print_processors_stats()

    print("\nRegistering other data processors")
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    print("Send the batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print(
        "\nConsume some elements from the data processors:"
        " Numeric 3, Text 2, Log 1"
    )

    for i in range(3):
        ds.processors[0].output()
    for i in range(2):
        ds.processors[1].output()
    for i in range(1):
        ds.processors[2].output()

    ds.print_processors_stats()
