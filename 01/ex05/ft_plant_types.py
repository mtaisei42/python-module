class Plant:
    def __init__(self, name :str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
    def show(self):
        print("{self.name}: {self._height:.1f}cm, {self._age} days old")
class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.is_bollom = False
    def bloom(self):
        self.is_bollom = True
    def show(self):
        super().show
        print(f"Color; {self.color}")
        if self.is_bollom:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")
class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def show(self):
        super().show()