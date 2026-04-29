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
        self.count += 1
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
        else:
            self.storage.append(str(data))


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


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    print()

    input1 = 42
    np_input2 = 'Hello'
    np = NumericProcessor()

    print(f"Trying to validate input '{input1}': {np.validate(input1)}")
    print(f"Trying to validate input '{np_input2}': {np.validate(np_input2)}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest('foo')
    except ValueError as e:
        print(f"Got exception: {e}")

    print("Processing data: [1, 2, 3, 4, 5]")

    np.ingest([1, 2, 3, 4, 5])

    print("Extracting 3 values...")

    for i in range(3):
        rank, val = np.output()
        print(f"Numeric value {rank}: {val}")
    print("\nTesting Text Processor...")
    print()

    tp = TextProcessor()

    print(f"Trying to validate input {input1}: {tp.validate(input1)}")

    print("Processing data: ['Hello', 'Nexus', 'World']")

    tp.ingest(['Hello', 'Nexus', 'World'])
    print("Extracting 1 value...")

    rank, val = tp.output()
    print(f"Text value {rank}: {val}")
    print("\nTesting Log Processor...")
    print()

    lp = LogProcessor()
    print(f"Trying to validate input 'Hello': {lp.validate('Hello')}")

    logs = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
        ]
    print(f"Processing data: {logs}")

    lp.ingest(logs)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = lp.output()
        print(f"Log entry {rank}: {val}")
