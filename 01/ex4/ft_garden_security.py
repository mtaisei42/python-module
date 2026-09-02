class Plant:
    def __init__(self, name :str, height: float, age: int):
        self.name = name
        self._height = height
        self._age = age

    def show(self):
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def set_height(self, new_height: float) -> bool:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return False
        self._height = new_height
        print(f"Height updated: {self._height:.0f}cm")
        return True

    def set_age(self, new_age) -> bool:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return False
        self._age = new_age
        print(f"Age updated: {self._age} days")
        return True
    

    def get_height(self):
        return (self._height)


    def get_age(self):
        return (self._age)


def ft_garden_security():
    Rose = Plant("Rose", 15, 10)
    print("Plant created:", end = " ")
    Rose.show()
    print("=== Garden Security System ===")
    Rose.set_height(25)
    Rose.set_age(30)
    Rose.set_height(-5.0)
    Rose.set_age(-10)
    print("Current state:", end=" ")
    Rose.show()


ft_garden_security()
