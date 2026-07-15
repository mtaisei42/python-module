def secure_archive(
        file_name: str, option: str, content: str = ""
) -> tuple[bool, str]:
    try:
        if option == "read":
            with open(file_name, "r") as f:
                data = f.read()
                return(True, data)
        elif option == "write":
            with open(file_name, "w") as f:
                f.write(content)
                return(True, "Content successfully written to file")
        else:
            return(False, "Invalid option")
    except OSError as e:
        return(False, str(e))


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
    print(secure_archive("new_archive.txt", "write", result[1]))

main()
