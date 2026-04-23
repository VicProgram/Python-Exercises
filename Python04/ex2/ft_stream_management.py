import sys
from typing import IO


def display_file(file: str) -> str:
    try:
        f: IO[str] = open(file, "r")
        content = f.read()
        print("---")
        print()
        print(content)
        if not content.endswith('\n'):
            print()
        print()
        print("---")
        f.close()
        print()
        print(f"File '{file}' closed.\n")
        return content
    except (FileNotFoundError, PermissionError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{file}': {e}\n")
        return ""


def transform_data(content: str, filename: str) -> None:

    print("Transform data:")
    print("---\n")

    lines = content.split("\n")

    for line in lines:
        if line:
            print(line + "#")

    print("---\n")


def save_data(content: str, filename: str) -> None:

    if filename == "":
        sys.stdout.write("Not saving data.")
        return

    print(f"Saving data to '{filename}'")
    try:
        f: IO[str] = open(filename, "w")
        lines = content.split("\n")
        for line in lines:
            if line:
                f.write(line + "#\n")
        f.close()
        sys.stdout.write(f"Data saved in file '{filename}'.")
        sys.stdout.flush()
    except (FileNotFoundError, PermissionError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stderr.write("Data not saved")
        sys.stderr.flush()


if __name__ == "__main__":

    print("=== Cyber Archives Recovery & Preservation  ===")

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)

    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")

    content = display_file(file_name)

    if content is not None:

        transform_data(content, file_name)
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        filename = sys.stdin.readline().strip()
        if filename is not None:
            save_data(content, filename)
