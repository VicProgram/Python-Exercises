class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")

    def grow(self, cm) -> int:
        self._height += cm
        return cm

    def plusday(self) -> None:
        self._age += 1

    def set_height(self, cm):
        if cm < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height updated rejected")
            return
        self._height = cm

    def set_age(self, days):
        if days < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age updated rejected")
            return
        self._age = days

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def print_sec(plant):
        print(" === Garden Security System === ")
        print("Plant created: ", end=" ")
        plant.show()
        print()
        plant.set_height(25)
        plant.set_age(30)
        print(f"Height updated: {plant.get_height()}")
        print(f"Age updated: {plant.get_height()}")
        print()
        plant.set_height(-25)
        plant.set_age(-12)
        print()
        print(
            f"Current state: {plant.name}: "
            f"{plant.get_height()}cm, {plant.get_age()} days old"
        )


if __name__ == "__main__":

    rose = Plant("Rose", 15.0, 10)

    Plant.print_sec(rose)
