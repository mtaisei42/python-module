class plant:
    def __init__(self, name :str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
    def show(self):
        print(f"{self.name}: {self.height: .1f}cm, {self.age} days old")
    def grow(self):
        self.height += 0.8
    def age_one_day(self):
        self.age += 1

def ft_plant_growth():
    Rose = plant("Rose", 25, 30)
    start_height = Rose.height
    print("=== Garden Plant Growth ===")
    Rose.show()
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        Rose.grow()
        Rose.age_one_day()
        Rose.show()
    growth = Rose.height - start_height
    print(f"Growth this week: {round(growth, 1)}cm")

ft_plant_growth()