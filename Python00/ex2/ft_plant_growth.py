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

    def plusday(self) -> None:
        self.age += 1


if __name__ == "__main__":

    rose = Plant("Rose", 25.0, 30)
    sunflower = Plant("Sunflower", 80.0, 45)
    cactus = Plant("Cactus", 15.0, 120)

    def pass_week(plant_growing) -> None:
        total_growth: float = 0.0
        print(" === Garden Plant Growth === ")
        for i in range(1, 8):
            print(f" === Day {i} === ")
            plant_growing.show()
            day_growth = rose.grow(0.8)
            plant_growing.plusday()
            total_growth += day_growth
        print(f" === Growth this week: {round(total_growth)}cm === ")

    pass_week(rose)
