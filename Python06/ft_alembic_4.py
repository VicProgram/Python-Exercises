import alchemy

if __name__ == "__main__":

    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air: Air element created")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")

    try:
        print(alchemy.create_air())

        # print(alchemy.create_earth())
    except Exception as e:
        print(f"{e}")
