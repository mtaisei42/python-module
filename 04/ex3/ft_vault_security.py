def secure_archive(
        file_name: str, option: str = "read", content: str = ""
) -> tuple[bool, str]:
    try:
        if option == "read":
            with open(file_name, "r") as f:
                data = f.read()

        elif option == "write":
            with open(file_name, "w") as f:
                f.write(content)
                return True, "Content successfully written to file"
        else:
            return False, "Invalid option"
    except (OSError, UnicodeError) as e:
        return False, str(e)

    print(f.closed)
    return True, data

    


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    result: tuple[bool, str] = secure_archive("ancient_fragment.txt", "read")
    print(result)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("new_archive.txt", "write", result[1]))
    else:
        print("Data not saved because the source could not be read.")


if __name__ == "__main__":
    main()
