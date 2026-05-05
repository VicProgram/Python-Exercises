from ex0 import AquaFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex2 import StrategyFail
from typing import Any


def battle(opponents: list[tuple[Any, Any]]) -> None:
    fighters = []

    for factory, strategy in opponents:
        creature_instance = factory.create_base()
        fighters.append((creature_instance, strategy))

    print("*** Tournament ***")
    print(f"{len(fighters)} opponents involved")

    n = len(fighters)

    for i in range(n):
        for j in range(i + 1, n):
            c1, s1 = fighters[i]
            c2, s2 = fighters[j]

            print("* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")

            try:
                for msg in s1.act(c1):
                    print(msg)
                for msg in s2.act(c2):
                    print(msg)
            except StrategyFail as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    combats0 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        ]

    combats1 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]

    combats2 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]

    print("Tournament 0 (basic)")
    battle(combats0)

    print("\nTournament 1 (error)")
    battle(combats1)

    print("\nTournament 2 (multiple)")
    battle(combats2)


if __name__ == "__main__":
    main()
