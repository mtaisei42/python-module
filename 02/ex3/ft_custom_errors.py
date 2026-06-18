#!usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message="A garden error occurred"):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message="Unknown plant error occurred"):
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message="Unknown water error occurred"):
        super().__init__(message)

def check_plant_health(plant_name, status):
    if status == "wilting":
        raise PlantError(f"The {plant_name} plant is wilting!")

def check_water_tank(level):
    if level < 10:
        raise WaterError("Not enough water in the tank!")

def test_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        check_plant_health("tomato", "wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        check_water_tank(3)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        check_plant_health("tomato", "wilting")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water_tank(3)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")

if __name__ == "__main__":
    test_custom_errors()
