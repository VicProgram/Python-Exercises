import sys
import os
import site


def check_virtual_env() -> None:

    python_path = sys.executable
    if sys.prefix != sys.base_prefix:

        python_path2 = sys.prefix
        python_name = os.path.basename(sys.prefix)
        python_package = site.getsitepackages()

        print("MATRIX STATUS: Welcome to construct\n")
        print(f"Current Python: {python_path}")
        print(f"Virtual Enviroment: {python_name}")
        print(f"Enviroment Path: {python_path2}\n")

        print(
            "SUCCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting\n"
            "the global system."
        )

        print(f"Package installation path: \n{python_package[0]}")

    else:

        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {python_path}")
        print("Virtual Enviroment: None detected\n")
        print(
            "WARNING: You're in the global environment!\n"
            "The machines can see everything you install."
        )

        print(
            "\nTo enter the construct, run:"
            "\npython -m venv matrix_env"
            "\nsource matrix_env/bin/activate # On Unix\n"
            "matrix_env\Scripts\activate # On Windows"
        )
        print("\nThen run this program again.")
        return


def main() -> None:

    check_virtual_env()


if __name__ == "__main__":
    main()
