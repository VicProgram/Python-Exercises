class Plant:

    class Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0
            self._shade_calls: int = 0

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._stats = Plant.Stats()

    def show(self) -> None:
        self._stats._show_calls += 1
        print(
            f"{self._name}: {round(self._height, 1)}cm,"
            f" {self._age} days old"
        )

    def grow(self, cm: float = 2.0) -> float:
        self._stats._grow_calls += 1
        self._height += cm
        return cm

    def age(self) -> None:
        self._stats._age_calls += 1
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

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls(name="Unknown plant", height=0.0, age=0)


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

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def __init__(self, trunk_diameter: float, **kwargs) -> None:
        super().__init__(**kwargs)
        self._trunk_diameter = trunk_diameter
        self._stats = Tree.Stats()

    def produce_shade(self) -> None:
        self._stats._shade_calls += 1
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self._height, 1)}cm long and "
            f"{self._trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, harvest_season: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self._harvest_season = harvest_season
        self._nutritional_value: int = 0

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


class Seed(Flower):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


def display_stats(plant: Plant) -> None:
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()

    print("=== Flower")
    rose = Flower(color="red", name="Rose", height=15.0, age=10)
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print()

    print("=== Tree")
    oak = Tree(trunk_diameter=5.0, name="Oak", height=200.0, age=365)
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)
    print()

    print("=== Seed")
    sunflower = Seed(color="yellow", name="Sunflower", height=80.0, age=45)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)
    print()

    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    display_stats(unknown)
