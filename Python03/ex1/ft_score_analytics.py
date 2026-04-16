# #! /usr/bin/env python3

# import sys


# def ft_score_analytics(scorelist: list) -> None:
#     scores = scorelist
#     total_players = len(scores)
#     total_score = sum(scores)
#     average = total_score / total_players
#     high_score = max(scores)
#     low_score = min(scores)

#     print("=== Player Score Analytics ===")
#     print("Total players: ", total_players)
#     print(f"Total score: {total_score}")
#     print(f"Average score:{average:.1f}")
#     print(f"High score: {high_score}")
#     print(f"Low score: {low_score}")
#     print(f"Score range: {high_score - low_score}")


# if __name__ == "__main__":
#     # ft_score_analytics()
#     scorelist = []
#     if len(sys.argv) == 1:
#         print(
#             "No scores provided. Usage: python3 "
#             "ft_score_analytics.py < score1> <score2> ..."
#         )
#     else:
#         for arg in sys.argv[1:]:
#             try:
#                 arg = int(arg)
#                 scorelist.append(arg)
#             except ValueError:
#                 print("Invalid parameter")
#     if scorelist:
#         ft_score_analytics(scorelist)

def ft_score_analytics(scorelist: list) -> None:
    
    if len(sys.argv) == 1:
            print(
                "No scores provided. Usage: python3 "
                "ft_score_analytics.py < score1> <score2> ..."
            )
    try:
        for arg in sys.argv[1:]:
            scores += arg
        
if __name__ == "__main__":
    ft_score_analytics()