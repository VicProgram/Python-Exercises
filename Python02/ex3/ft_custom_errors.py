class GardenError(Exception):
    def __init__(self, mensaje: str = ("Unknown garden error: ")) -> None:
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class WaterError(GardenError):
    def __init__(self, mensaje: str = ("Unknown water error")) -> None:
        super().__init__(mensaje)


class PlantError(GardenError):
    def __init__(self, mensaje: str = ("Unknown plant error")) -> None:
        super().__init__(mensaje)


def werror(liters: int) -> None:
    if liters < 10:
        raise WaterError(" Not enought water in the tank!")


def perror(wilt: bool, plant_name: str) -> None:
    if wilt:
        raise PlantError(f"The {plant_name} is wilting!")


if __name__ == "__main__":

    print("Testing PlantError")
    try:
        perror(True, "Tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError")
    try:
        werror(8)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    try:
        werror(8)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        perror(True, "Tomato")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print()
    print("All custom error types work correctly!")
