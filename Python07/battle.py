from ex0.factory import FlameFactory, AquaFactory


def main() -> None:

    ff = FlameFactory()
    af = AquaFactory()

    mon = ff.create_base()
    mon1 = ff.create_evolved()
    mon2 = af.create_base()
    mon3 = af.create_evolved()

    print("Testing Factory")
    print(mon.describe())
    print(mon.attack())

    print(mon1.describe())
    print(mon1.attack())

    print("\nTesting Factory")

    print(mon2.describe())
    print(mon2.attack())

    print(mon3.describe())
    print(mon3.attack())

    print("\nTesting Battle")
    print(f"{mon.name} is a {mon.creature_type} type Creature")
    print("vs.")
    print(f"{mon2.name} is a {mon2.creature_type} type Creature")

    print("fight!")
    print(f"{mon.attack()}")
    print(f"{mon2.attack()}")


if __name__ == "__main__":
    main()
