class PlantError(Exception):
    def __init__(self, mensaje: str = ("Unknown plant error")) -> None:
        super().__init__(mensaje)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}")
    print(f"Watering {plant_name}: [OK]")


lista = ("Tomato", "Letucce", "Carrots")
lista1 = ("Tomato", "letucce")


def tetsing_watering(lista: tuple[str, ...]) -> None:
    print("Testing valid plants...")
    print("Opening watering system")
    for plant in lista:
        try:
            water_plant(plant)
        except PlantError as e:
            print(f"Caught PlantError: {e}")
        finally:
            print("Closing watering system")
    print()
    print("Testing invalid plants...")
    print("Opening watering system")
    for plant in lista1:
        try:
            water_plant(plant)
        except PlantError as e:
            print(f"Caught PlantError: {e}")
            print(".. ending test and returning to main")
        finally:
            print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    tetsing_watering(lista)
    print()
    print("Cleanup always happens, even with errors!")
