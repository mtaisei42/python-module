import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    file_name = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")
    try:
        file: typing.IO[str] = open(file_name, "r")
        try:
            data = file.read()
        finally:
            file.close()
    except (OSError, UnicodeError) as e:
        print(f"Error accessing file '{file_name}': {e}")
        return

    print("---\n")
    print(data)
    print("\n---")
    print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
