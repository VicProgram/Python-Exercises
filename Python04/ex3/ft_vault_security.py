def secure_archive(
        file_name: str, command: str, content: str = ""
        ) -> tuple[bool, str]:

    try:
        if command == 'r':
            with open(file_name, "r") as f:
                content = f.read()
                return (True, content)
        elif command == 'w':
            with open(file_name, "w") as f:
                f.write(content)
                return (True, "Content successfully written to file")
        return (False, "Invalid action. Use 'r' for read or 'w' for write.")
    except (FileNotFoundError, PermissionError) as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", 'r'))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", 'r'))

    print("Using 'secure_archive' to read from a regular file:")
    res_read = secure_archive("ancient_fragment.txt", 'r')
    print(res_read)

    print("Using 'secure_archive' to write previous content to a new file:")

    if res_read[0]:
        print(secure_archive("vault_copy.txt", 'w', res_read[1]))
    else:
        print(
            secure_archive("vault_copy.txt", 'w', "Data storage sequence...")
        )
