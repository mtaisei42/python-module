class plant:
    def __init__(self, name :str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data():
    rose = plant("Rose", 25, 30)
    sunflower = plant("Sunflower", 80, 45)
    cactus = plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()

ft_garden_data()
