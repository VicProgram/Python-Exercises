#! /usr/bin/env python3


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

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


class Tree(Plant):
    def __init__(
        self,
        wood_type: str,
        trunk_diameter: float,
        produce_shade: bool,
        **kwargs,
    ) -> None:

        super().__init__(**kwargs)
        self.wood_type = wood_type
        self.trunk_diameter = trunk_diameter
        self.produce_shade = produce_shade

        produce_shade = False

    def produce_shade(self) -> None:
        print(f"[Asking the {self.name} to produce shade]")
        self.produce_shade = True

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter} cm wide")
        if self.produce_shade:
            print(
                f"Tree {self.name} now produces a shade of "
                f"{self._height}cm long and {self.trunk_diameter}cm wide"
            )
        else:
            print("The tree doesn´t produce shade")


class Vegetable(Plant):
    def __init__(
        self,
        harvest_season: str,
        nutritional_value: int,
        **kwargs,
    ) -> None:

        super().__init__(**kwargs)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def set_age(self, age):
        super().set_age(age)
        if self.get_age() < 20:
            self.nutritional_value = 0
        else:
            self.nutritional_value = 20


class Flower(Plant):
    def __init__(
        self,
        color: str,
        blooming: bool,
        **kwargs,
    ) -> None:

        super().__init__(**kwargs)
        self.color = color
        self.blooming = blooming

        blooming = False

    def bloom(self) -> None:
        self.blooming = True
        print(f"[asking the {self.name} to bloom]")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.blooming:
            print(f"{self.name} is blooming beautifully")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, **kwargs):

        self.number_of_seeds = 0
        super().__init__(**kwargs)

    def seed_bloom(self, age) -> None:

        if not self.blooming:
            self.blooming = True
            self.number_of_seeds = 42
            self.set_age(age)


if __name__ == "__main__":

    rose = Flower("red", False, name="Rose", height=15.0, age=10)
    oak = Tree("Brrown", 5.00, 5.0, name="Oak", height=200.0, age=365)
    sunflower = Seed(
        color="yellow", blooming=False, name="Sunflower", height=80.0, age=45
    )
    print("=== Check year-old ===")
    # Plant.age_checker(361)

    # new = Plant.create_anonymous()
    # new.show()

    # rose.bloom()
    sunflower.show()
    sunflower.seed_bloom(50)
    sunflower.show()
