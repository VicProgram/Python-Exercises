import math


def calculate_distance(
    coords1: tuple[float, float, float],
    coords2: tuple[float, float, float] = (0.0, 0.0, 0.0),
) -> float:

    x1, y1, z1 = coords1
    x2, y2, z2 = coords2

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    return distance


def get_player_pos() -> tuple[float, float, float]:
    while True:
        values = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = values.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        coords = []
        is_valid = True

        for value in parts:
            value = value.strip()
            try:
                coords.append(float(value))
            except ValueError as e:
                print(f"Error on parameter '{value}': {e}")
                is_valid = False
                break

        if is_valid:
            return (coords[0], coords[1], coords[2])


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()

    print("Get a first set of coordinates")
    coords1 = get_player_pos()

    print(f"Got a first tuple: {coords1}")
    x1, y1, z1 = coords1
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    center_distance = calculate_distance(coords1)
    print(f"Distance to center: {center_distance:.4f}")
    print()

    print("Get a second set of coordinates")
    coords2 = get_player_pos()

    distance = calculate_distance(coords1, coords2)
    print(f"Distance between the 2 sets of coordinates: {distance:.4f}")
