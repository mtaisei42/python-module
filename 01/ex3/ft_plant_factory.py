class plant:
    def __init__(self, name :str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
    def show(self):
        print(f"Created: {self.name}: {self.height: .1f}cm, {self.age} days old")

def ft_plant_factory():
    Rose = plant("Rose", 25, 30)
    Oak = plant("Oak", 200, 365)
    Cactus = plant("Cactus", 5, 90)
    Sunflower = plant("Sunflower", 80, 45)
    Fern = plant("Fern", 15, 120)
    print("=== Plant Factory Output ===")
    Rose.show()
    Oak.show()
    Cactus.show()
    Sunflower.show()
    Fern.show()

ft_plant_factory()
