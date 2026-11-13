import sys


def main() -> None:

    print("=== Player Score Analytics ===")

    file_name, *score_args = sys.argv
    valid_scores = []
    invalid_scores = []

    for arg in score_args:
        try:
            valid_scores.append(int(arg))
        except ValueError:
            invalid_scores.append(arg)

    for inval in invalid_scores:
        print(f"Invalid parameter:'{inval}'")

    if not valid_scores:
        print(f"No scores provided. Usage: python3 "
              f"{file_name} <score1> <score2> ...")
        return

    total = len(valid_scores)
    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {total}")
    print(f"Total score: {sum(valid_scores)}")
    print(f"Average score: {sum(valid_scores) / total}")
    print(f"High score: {max(valid_scores)}")
    print(f"Low score: {min(valid_scores)}")
    print(f"Score range: {max(valid_scores) - min(valid_scores)}")


if __name__ == "__main__":
    main()
