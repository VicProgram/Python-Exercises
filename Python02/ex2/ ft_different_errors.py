def garden_operations(operation_number: int) -> None:
    print(f"Testing operation {operation_number}...")
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("text.txt")
    elif operation_number == 3:
        int("abc" + 5)
    else:
        return


def test_error_types() -> None:
    try:
        garden_operations(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    try:
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    try:
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    try:
        garden_operations(3)
    except (ValueError, TypeError) as e:
        print(f"Caught TypeError: {e}")
    try:
        garden_operations(4)
        print("Operation completed succesfully!")
    except Exception as e:
        print(f"Other exception {e}")


if __name__ == "__main__":
    print("=== Gardenb Error Types Demo ===")
    test_error_types()
    print()
    print("All error types tested succesfully!")
