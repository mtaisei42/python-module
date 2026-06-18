#!/usr/bin/env python3

def input_temperature(temp_str):
    temp_int = int(temp_str)
    if temp_int > 40:
        raise ValueError("100°C is too hot for plants (max 40°C)")
    elif temp_int < 0:
        raise ValueError("-50°C is too cold for plants (min 0°C)")
    print(f"Temperature is now {temp_int}°C")
def test_temperature():
    print(f"=== Garden Temperature Checker ===\n")

    print("Input data is '25'")
    try:
        input_temperature("25")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\nInput data is 'abc'")
    try:
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\nInput data is '100'")
    try:
        input_temperature("100")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\nInput data is '-50'")
    try:
        input_temperature("-50")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()
