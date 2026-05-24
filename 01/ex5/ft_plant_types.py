class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.is_bollom = False

    def bloom(self):
        self.is_bollom = True

    def show(self):
        super().show
        print(f"Color: {self.color}")
        if self.is_bollom:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self):
        print(f"Tree Oak now produces a shade of {self.height:.1f}cm", end="")
        print(f" long and {self.trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)
        self.Nut_val = 0
        self.season = "April"

    def show(self):
        super().show()
        print(f" Harvest season: {self.season}")
        print(f" Nutritional value: {self.Nut_val}")

    def next_age(self):
        self.age += 1

    def grow(self):
        self.height += 2.1
        self.Nut_val += 1


def ft_plant_types():
    Rose = Flower("Rose", 15.0, 10, "red")
    Oak = Tree("Oak", 200.0, 365, 5)
    Tomato = Vegetable("Tomato", 5.0, 10)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    Rose.show()
    print("[asking the rose to bloom]")
    Rose.bloom()
    Rose.show()
    print("\n")
    print("=== Tree")
    Oak.show()
    print("[asking the oak to produce shade]")
    Oak.produce_shade()
    print("\n")
    print("=== Vegetable")
    Tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        Tomato.grow()
        Tomato.next_age()
    Tomato.show()


ft_plant_types()
