import random


players = [
    'Alice', 'bob', 'Charlie', 'dylan',
    'Emma', 'Gregory', 'john', 'kevin', 'Liam'
]


cap_players = [player.capitalize() for player in players]
fcap_players = [player for player in players if player[0].isupper()]

achievements = {player: random.randint(1, 1000) for player in cap_players}

average = sum(achievements.values()) / len(achievements)

high_scores = {k: v for k, v in achievements.items() if v > average}

if __name__ == "__main__":

    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {cap_players}")
    print(f"New list of capitalized names only: {fcap_players}")
    print(f"Score dict: {achievements}")
    print(f"Score average is {round(average, 2)}")
    print(f"High scores: {high_scores}")
