import sys
import typing

def ft_archive_creation(data):
    print("Transform data:")
    lines = data.splitlines()
    new_data = ""
    for line in lines:
        line = line + "#\n"
        new_data += line
    print("---\n")
    print(new_data)
    print("\n---")
    file_name = input("Enter new file name (or empty): ")
    if file_name == "":
        print("Not saving data.")
        return
    try:
        f_out: typing.IO[str] = open(file_name, "w")
        try:
            f_out.write(new_data)
            print(f"Saving data to '{file_name}'")
            print(f"Data saved in file '{file_name}'.")
        finally:
            f_out.close()
    except OSError as e:
       print(f"Error opening file '{file_name}': {e}")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archibe_areation.py <file>")
        return
    file_name = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    try:
        file: typing.IO[str] = open(file_name, "r")
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
        return
    try:
        data = file.read()
        print("---\n")
        print(data)
        print("\n---")
    finally:
        file.close()
        print(f"File '{file_name}' closed.\n")

    ft_archive_creation(data)


main()
