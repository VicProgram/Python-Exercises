import sys
from typing import IO


def display_file(file: str) -> str:
    try:
        f: IO[str] = open(file, "r")
        content = f.read()
        print("---")
        print()
        print(content)
        print()
        print("---")
        f.close()
        print()
        print(f"File '{file}' closed.\n")
        return content
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{file}': {e}")
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
        print("Not saving data.")
        return

    print(f"Saving data to '{filename}'")
    f: IO[str] = open(filename, "w")
    lines = content.split("\n")
    for line in lines:
        if line:
            f.write(line + "#\n")
    f.close()
    print(f"Data saved in file '{filename}'.")


if __name__ == "__main__":

    print("=== Cyber Archives Recovery & Preservation ===")

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)

    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")

    content = display_file(file_name)
    
    transform_data(content, file_name)

    filename = input("Enter new file name (or empty): ")

    save_data(content, filename)
