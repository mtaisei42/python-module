#!usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message="A garden error occurred"):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message="Unknown plant error occurred"):
        super().__init__(message)

def water_plant(plant_name):
    cap_name = plant_name.capitalize()
    if cap_name == plant_name:
        print(f"Watering {cap_name} : [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

def test_watering_system():
    print("=== Garden Watering System ===\n")

    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    try:
        water_plant("Tomato")
        water_plant("lettuece")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("\nCleanup always happens, even with errors!")

test_watering_system()
