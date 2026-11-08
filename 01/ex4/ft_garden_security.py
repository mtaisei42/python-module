class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_age(age)
        self.set_height(height)

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def set_height(self, new_height: float) -> bool:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return False
        self._height = new_height
        print(f"Height updated: {self._height:.0f}cm")
        return True

    def set_age(self, new_age: int) -> bool:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return False
        self._age = new_age
        print(f"Age updated: {self._age} days")
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print("Plant created:", end=" ")
    rose.show()
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5.0)
    rose.set_age(-10)
    print("Current state:", end=" ")
    rose.show()


if __name__ == "__main__":
    ft_garden_security()
