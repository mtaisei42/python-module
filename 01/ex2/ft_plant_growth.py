class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self._age += 1


def ft_plant_growth() -> None:
    rose = Plant("Rose", 25, 30)
    start_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        rose.grow()
        rose.age()
        rose.show()
    growth = rose.height - start_height
    print(f"Growth this week: {round(growth, 1)}cm")


if __name__ == "__main__":
    ft_plant_growth()
