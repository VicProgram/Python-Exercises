from typing import Any, Protocol
from abc import ABC, abstractmethod


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        output = ",".join(item[1] for item in data)
        print(output)


class JSONExportPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")

        parts = [f'"item_{item[0]}": "{item[1]}"' for item in data]
        output = "{" + ", ".join(parts) + "}"
        print(output)


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
                self.count += 1
                self.storage.append(str(item))
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
            self.count += 1
            self.storage.append(item_entry)


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            nlst = []
            for _ in range(nb):
                try:
                    item = proc.output()
                    nlst.append(item)
                except IndexError:
                    break
            if nlst:
                plugin.process_output(nlst)


if __name__ == "__main__":

    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Processors")
    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    batch1 = [
        'Hello world', [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42, ['Hi', 'five']
        ]
    print(f"\nSend first batch of data on stream: {batch1}")
    ds.process_stream(batch1)
    ds.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, CSVExportPlugin())
    ds.print_processors_stats()

    batch2 = [
        21,
        [
            'I love AI',
            'LLMs are wonderful',
            'Stay healthy'
        ],
        [
            {
                'log_level': 'ERROR',
                'log_message': '500 server crash'
            },
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"\nSend another batch of data: {batch2}")
    ds.process_stream(batch2)
    ds.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, JSONExportPlugin())
    ds.print_processors_stats()
