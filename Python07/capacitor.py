from ex1.capabilities import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:

    hf = HealingCreatureFactory()
    tf = TransformCreatureFactory()

    print("Testing Creature with healing capability")

    mon5 = hf.create_evolved()
    mon4 = hf.create_base()
    mon6 = tf.create_base()
    mon7 = tf.create_evolved()

    print(" base:")
    print(f"{mon4.describe()}")
    print(f"{mon4.attack()}")
    print(f"{mon4.heal()}")  # type: ignore

    print(" evolved:")
    print(f"{mon5.describe()}")
    print(f"{mon5.attack()}")
    print(f"{mon5.heal()}")  # type: ignore

    print("\nTesting Creature with transform capability")
    print(" base:")
    print(f"{mon6.describe()}")
    print(f"{mon6.attack()}")
    print(f"{mon6.transform()}")  # type: ignore
    print(f"{mon6.attack()}")
    print(f"{mon6.revert()}")  # type: ignore
    print(" evolved:")
    print(f"{mon7.describe()}")
    print(f"{mon7.attack()}")
    print(f"{mon7.transform()}")  # type: ignore
    print(f"{mon7.attack()}")
    print(f"{mon7.revert()}")  # type: ignore


if __name__ == "__main__":
    main()
