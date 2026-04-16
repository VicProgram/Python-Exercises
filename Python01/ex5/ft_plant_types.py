class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height, 1)} cm"
            f"{self._age} days old"
        )

    def grow(self, cm: float = 2.0) -> float:
        self._height += cm
        return cm

    def age(self) -> None:
        self._age += 1

    def set_height(self, cm: float) -> None:
        if cm < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = cm

    def set_age(self, days: int) -> None:
        if days < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = days

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


class Flower(Plant):
    def __init__(self, color: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self._color = color
        self._blooming = False

    def bloom(self) -> None:
        self._blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, trunk_diameter: float, **kwargs) -> None:
        super().__init__(**kwargs)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self._height, 1)}cm long and"
            f"{self._trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, harvest_season: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self, cm: float = 2.0) -> float:
        result = super().grow(cm)
        self._nutritional_value += 1
        return result

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower(color="red", name="Rose", height=15.0, age=10)
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak = Tree(trunk_diameter=5.0, name="Oak", height=200.0, age=365)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable(
        harvest_season="April", name="Tomato",
        height=5.0, age=10
        )
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
