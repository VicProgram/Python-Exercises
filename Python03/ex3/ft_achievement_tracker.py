import random

achievements = [
    "Boss Slayer",
    "Collector Supreme",
    "Crafting Genius",
    "First Steps",
    "Hidden Path Finder",
    "Master Explorer",
    "Sharp Mind",
    "Speed Runner",
    "Strategist",
    "Survivor",
    "Treasure Hunter",
    "Unstoppable",
    "Untouchable",
    "World Savior",
]


def gen_player_achievements() -> set:

    number = random.randint(1, len(achievements))
    achieves = random.sample(achievements, number)

    return set(achieves)


if __name__ == "__main__":

    print("=== Achievement Tracker System ===")
    print()

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}\n")
    print(f"Player Bob: {bob}\n")
    print(f"Player Charlie: {charlie}\n")
    print(f"Player Dylan: {dylan}\n")
    all_achieves = alice.union(bob).union(charlie).union(dylan)

    print(f"All distinct achievemets: {all_achieves}\n")
    print()

    common = alice.intersection(bob).intersection(charlie).intersection(dylan)
    print(f"Common achievements: {common}\n")
    print()

    alice_diff = alice.difference(bob.union(charlie).union(dylan))
    bob_diff = bob.difference(alice.union(charlie).union(dylan))
    charlie_diff = charlie.difference(bob.union(alice).union(dylan))
    dylan_diff = dylan.difference(bob.union(charlie).union(alice))

    print(f"Only Alice has: {alice_diff}")
    print(f"Only Bob has: {bob_diff}")
    print(f"Only Charlie has: {charlie_diff}")
    print(f"Only Dylan has: {dylan_diff}")
    print()

    alice_missing = set(achievements).difference(alice)
    bob_missing = set(achievements).difference(bob)
    charlie_missing = set(achievements).difference(charlie)
    dylan_missing = set(achievements).difference(dylan)

    print(f"Alice is missing: {alice_missing}")
    print(f"Bob is missing: {bob_missing}")
    print(f"Charlie is missing: {charlie_missing}")
    print(f"Dylan is missing: {dylan_missing}")
