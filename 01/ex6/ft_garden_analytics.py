class Plant:
    class Statistics:
        def __init__(self):
            self.grow_colls = 0
            self.age_colls = 0
            self.show_colls = 0

        def count_grow(self):
            self.grow_colls += 1

        def count_age(self):
            self.age_colls += 1

        def count_show(self):
            self.show_colls += 1

        def show(self):
            print(
                f"Stats: {self.grow_colls} grow, "
                f"{self.age_colls} age "
                f"{self.show_colls} show"
            )
            
    def __init__(self, name: str, height: float, Age: int):
        self.name = name
        self.height = height
        self.Age = Age
        self.stats = Plant.Statistics()

    def show(self):
        self.stats.count_show()
        print(f"{self.name}: {self.height:.1f}cm, {self.Age} days old")

    @staticmethod
    def year_old(days: int):
        return days > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unkown plant", 0.0, 0)

    def show_statistics(self):
        self.stats.show()

class Flower(Plant):
    def __init__(self, name, height, Age, color):
        super().__init__(name, height, Age)
        self.color = color
        self.is_bloom = False

    def bloom(self):
        self.is_bloom = True

    def age(self):
        self.Age += 1
        self.stats.count_age()

    def grow(self):
        self.height += 1
        self.stats.count_grow()

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if self.is_bloom:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")
    def show_statistics(self):
        self.stats.show()


class Tree(Plant):
    def __init__(self, name, height, Age, trunk_diameter: float):
        super().__init__(name, height, Age)
        self.trunk_diameter = trunk_diameter
        self.shade_calls = 0

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def age(self):
        self.Age += 1
        self.stats.count_age()

    def grow(self):
        self.height += 1
        self.stats.count_grow()

    def produce_shade(self):
        self.shade_calls += 1
        print(f"Tree Oak now produces a shade of {self.height:.1f}cm", end="")
        print(f" long and {self.trunk_diameter:.1f}cm wide.")

    def show_statistics(self):
        self.stats.show()
        print(f" {self.shade_calls} shade")


class Vegetable(Plant):
    def __init__(self, name, height, Age, harvest_season):
        super().__init__(name, height, Age)
        self.Nut_val = 0
        self.harvest_season = harvest_season

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.Nut_val}")

    def age(self):
        self.stats.count_age()
        self.Age += 1

    def grow(self):
        self.stats.count_grow()
        self.height += 2.1
        self.Nut_val += 1

    def show_statistics(self):
        self.stats.show()


class Seed(Flower):
    def __init__(self, name, height, Age, color):
        super().__init__(name, height, Age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def grow(self):
        self.height += 1.5
        self.stats.count_grow()

    def show(self):
        super().show()
        print(f" Seeds: {self.seeds}")

    def age(self):
        self.Age += 1
        self.stats.count_age()

    def show_statistics(self):
        self.stats.show()

def display_statistics(plant: Plant):
    print(f"[statistics for {plant.name}]")
    plant.show_statistics()

def ft_garden_analytics():
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
    Rose = Flower("Rose", 10, 15.0, "red")
    Rose.show()
    display_statistics(Rose)
    print("[asking the rose to grow and bloom]")
    Rose.bloom()
    Rose.show()
    display_statistics(Rose)
    print("\n")
    print("=== Tree")
    Oak = Tree("Oak", 200.0, 365, 5.0)
    Oak.show()
    display_statistics(Oak)
    print("[asking the oak to produce shade]")
    Oak.produce_shade()
    print("[statistics for Oak]")
    display_statistics(Oak)
    print("\n")
    print("=== Seed")
    Sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    Sunflower.show()
    print("[make sunflower grow, age and bloom]")
    Sunflower.bloom()
    for _ in range(20):
        Sunflower.age()
        Sunflower.grow()
    Sunflower.show()
    display_statistics(Sunflower)
    print("\n")
    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_statistics(unknown)

if __name__ == "__main__":
    ft_garden_analytics()
