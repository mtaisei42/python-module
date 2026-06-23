import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    file_name= sys.argv[1]
    print("=== ccyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")
    try:
        file: typing.IO[str] = open(file_name, "r")
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
        return

    date = file.read()
    print("---\n")
    print(f"{date}")
    print("\n---")
    file.close()
    print(f"File '{file_name}' closed.")


main()
