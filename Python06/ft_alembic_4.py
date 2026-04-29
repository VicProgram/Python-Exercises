import alchemy

if __name__ == "__main__":

    try:
        print(alchemy.create_air())

        print(alchemy.create_earth())
    except Exception as e:
        print(f"{e}")
