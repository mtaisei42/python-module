import random


def main() -> None:
    players = ["Alice", "bob", "Charlie", "dylan", "Emma",
                        "Gregory", "jhon", "kevin", "Lian"]

    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")

    cap_players = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {cap_players}")

    cap_only_players = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: "
          f"{cap_only_players}\n")

    score_dict = {name: random.randrange(50, 1000) for name in cap_players}
    print(f"Score dict: {score_dict}")
    score_av = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {score_av}")
    High_score_plyaers = {
        name: score for name, score in score_dict.items() if score > score_av
        }
    print(f"High scores: {High_score_plyaers}")


if __name__ == "__main__":
    main()
