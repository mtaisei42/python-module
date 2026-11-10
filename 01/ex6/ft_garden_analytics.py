#!/usr/bin/env python3
class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def count_grow(self) -> None:
            self._grow_calls += 1

        def count_age(self) -> None:
            self._age_calls += 1

        def count_show(self) -> None:
            self._show_calls += 1

        def show(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age
        self._stats = Plant.Statistics()

    def show(self) -> None:
        self._stats.count_show()
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    @staticmethod
    def year_old(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show_statistics(self) -> None:
        self._stats.show()


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_bloom = False

    def bloom(self) -> None:
        self.is_bloom = True

    def age(self) -> None:
        self._age += 1
        self._stats.count_age()

    def grow(self) -> None:
        self.height += 1
        self._stats.count_grow()

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_bloom:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def show_statistics(self) -> None:
        self._stats.show()


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._shade_calls = 0

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def age(self) -> None:
        self._age += 1
        self._stats.count_age()

    def grow(self) -> None:
        self.height += 1
        self._stats.count_grow()

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(
            f"Tree {self.name} now produces a shade of {self.height:.1f}cm",
            end="",
        )
        print(f" long and {self.trunk_diameter:.1f}cm wide.")

    def show_statistics(self) -> None:
        self._stats.show()
        print(f" {self._shade_calls} shade")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.nutritional_value = 0
        self.harvest_season = harvest_season

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def age(self) -> None:
        self._stats.count_age()
        self._age += 1

    def grow(self) -> None:
        self._stats.count_grow()
        self.height += 2.1
        self.nutritional_value += 1

    def show_statistics(self) -> None:
        self._stats.show()


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def grow(self) -> None:
        self.height += 1.5
        self._stats.count_grow()

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")

    def age(self) -> None:
        self._age += 1
        self._stats.count_age()

    def show_statistics(self) -> None:
        self._stats.show()


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.show_statistics()


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    if Plant.year_old(30):
        print("Is 30 days more than a year? -> True")
    else:
        print('Is 30 days more than a year? -> False')
    if Plant.year_old(400):
        print("Is 400 days more than a year? -> True")
    else:
        print("Is 400 days more than a year? -> False")
    print("\n")
    print("=== Flower")
    rose = Flower("Rose", 10, 15, "red")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.grow()
    rose.show()
    display_statistics(rose)
    print("\n")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)
    print("\n")
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.bloom()
    for _ in range(20):
        sunflower.age()
        sunflower.grow()
    sunflower.show()
    display_statistics(sunflower)
    print("\n")
    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_statistics(unknown)


if __name__ == "__main__":
    ft_garden_analytics()
