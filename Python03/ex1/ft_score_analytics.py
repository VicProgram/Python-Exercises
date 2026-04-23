import sys


def ft_score_analytics() -> None:

    nsp: str = "No scores provided. Usage: python3 "
    "ft_score_analytics.py < score1> <score2> ..."

    if len(sys.argv) == 1:
        print(nsp)
        return
    score_list = []
    for arg in sys.argv[1:]:
        try:
            num = int(arg)
            score_list.append(num)

        except ValueError:
            print(f"Invalid parameter '{arg}'")
    if score_list:
        print_score(score_list)
    else:
        print(nsp)


def print_score(score_list: list[int]) -> None:

    total_players = len(score_list)
    total_score = sum(score_list)
    average = total_score / total_players
    high_score = max(score_list)
    low_score = min(score_list)

    print("=== Player Score Analytics ===")
    print("Total players: ", total_players)
    print(f"Total score: {total_score}")
    print(f"Average score:{average:.1f}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {high_score - low_score}")


if __name__ == "__main__":
    ft_score_analytics()
