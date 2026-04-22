import sys
from typing import IO


# python3 ft_ancient_text.py /etc/shadow

def display_file(file: str) -> None:
    try:
        f: IO[str] = open(file, "r")
        content = f.read()
        print("---")
        print()
        print(content)
        print()
        print("---")
        f.close()
        print(f"File '{file}' closed.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{file}': {e}")


if __name__ == "__main__":

    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)
    f = sys.argv[1]
    print(f"Accessing file '{f}'")
    display_file(f)
