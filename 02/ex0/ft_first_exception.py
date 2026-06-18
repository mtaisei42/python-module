#!/usr/bin/env python3

def input_temperature(temp_str):
    print(f"Input data is '{temp_str}'")
    try:
        nbr = int(temp_str)
        print(f"Temperature is now {nbr}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

def test_temperture():
    print("=== Garden Temperature ===\n")
    input_temperature("25")
    input_temperature("abc")
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    try:
        test_temperture()
    except Exception as e:
        print(f"Error: {e}")
