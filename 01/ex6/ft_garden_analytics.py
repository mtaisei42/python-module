class Plant:
    show_count = 0
    age_count = 0
    grow_count = 0
    def __init__(self, name: str, height: float, Age: int):
        self.name = name
        self.height = height
        self.Age = Age

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.Age} days old")

    @staticmethod
    def year_old(days: int):
        return(days > 365)

    @classmethod
    def age_plus(cls):
        cls.age_count += 1

    @classmethod
    def statistics(cls):
        print(f"Stats: ")

class Flower(Plant):
    show_count = 0
    age_count = 0
    grow_count = 0
    def __init__(self, name, height, Age, color):
        super().__init__(name, height, Age)
        self.color = color
        self.is_bloom = False

    def bloom(self):
        self.is_bloom = True

    def age(self):
        self.Age += 1
        Flower.age_plus()

    def grow(self):
        self.height += 1

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.is_bloom:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, Age, trunk_diameter: float):
        super().__init__(name, height, Age)
        self.trunk_diameter = trunk_diameter

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self):
        print(f"Tree Oak now produces a shade of {self.height:.1f}cm", end="")
        print(f" long and {self.trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(self, name, height, Age):
        super().__init__(name, height, Age)
        self.Nut_val = 0
        self.season = "April"

    def show(self):
        super().show()
        print(f" Harvest season: {self.season}")
        print(f" Nutritional value: {self.Nut_val}")

    def age(self):
        self.Age += 1

    def grow(self):
        self.height += 2.1
        self.Nut_val += 1
