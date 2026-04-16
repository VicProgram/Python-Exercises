def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    list = ["abc", "25"]

    for param in list:
        print(f"Input data is {param}")
        try:
            print(f"Temperature is now {input_temperature(param)} ºC")
        except ValueError as e:
            print(f"Caught input_temperature error:  {e}")

    print("All test completed - program didn't crash")


if __name__ == "__main__":
    test_temperature()
