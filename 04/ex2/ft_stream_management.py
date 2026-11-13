import sys
import typing


def ft_archive_creation(data: str) -> None:
    print("Transform data:")
    lines = data.splitlines()
    new_data = ""
    for line in lines:
        line = line + "#\n"
        new_data += line
    print("---\n")
    print(new_data)
    print("\n---")
    try:
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        file_name = sys.stdin.readline().rstrip("\n")
    except (OSError, UnicodeError) as e:
        sys.stderr.write(f"[STDERR] Error reading input: {e}\n")
        sys.stderr.write("Data not saved.\n")
        return
    if file_name == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{file_name}'")
    try:
        f_out: typing.IO[str] = open(file_name, "w")
        try:
            f_out.write(new_data)
        finally:
            f_out.close()
    except (OSError, UnicodeError) as e:
        sys.stderr.write(f"[STDERR] Error saving file '{file_name}': {e}\n")
        sys.stderr.write("Data not saved.\n")
        return
    print(f"Data saved in file '{file_name}'.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return
    file_name = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    try:
        file: typing.IO[str] = open(file_name, "r")
        try:
            data = file.read()
        finally:
            file.close()
    except (OSError, UnicodeError) as e:
        sys.stderr.write(f"[STDERR] Error accessing file '{file_name}': {e}\n")
        return
    print("---\n")
    print(data)
    print("\n---")
    print(f"File '{file_name}' closed.\n")

    ft_archive_creation(data)


if __name__ == "__main__":
    main()
