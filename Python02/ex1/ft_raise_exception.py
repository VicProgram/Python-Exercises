def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int >= 40:
        raise ValueError(f"{temp_int}ºC is too hot for plants (max 40ºC) ")
    elif temp_int <= 0:
        raise ValueError(f"{temp_int}ºC is too cold for plants (min 0ºC)")
    else:
        return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()

    list = ["abc", "100", "-50"]

    for param in list:
        print(f"Input data is {param}")
        try:
            print(f"Temperature is now {input_temperature(param)} ºC")
            print()
        except ValueError as e:
            print(f"Caught input_temperature error:  {e}")
            print()
    print("All test completed - program didn't crash")


if __name__ == "__main__":
    test_temperature()
