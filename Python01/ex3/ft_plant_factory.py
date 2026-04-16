class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self, cm) -> int:
        self.height += cm
        return cm

    def plus_age(self) -> None:
        self.age += 1


if __name__ == "__main__":

    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)

    my_plants = [rose, oak, cactus, sunflower, fern]

    print(" === Plant Factory Output === ")
    for plant in my_plants:
        print("Created:", end=" ")
        plant.show()
