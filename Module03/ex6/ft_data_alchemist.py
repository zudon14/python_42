import random


def ft_data_alchemist() -> None:
    print("=== Game Data Alchemist ===\n")

    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    print(f"Initial list of players: {players}")

    # List comprehension 1: every name capitalized
    all_capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized}")

    # List comprehension 2: only the names that were already capitalized
    capitalized_only = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {capitalized_only}\n")

    # Dict comprehension 1: random score for each player
    scores = {name: random.randint(0, 1000) for name in all_capitalized}
    print(f"Score dict: {scores}")

    # The comparison uses the exact average; rounding is only for display
    average = sum(scores.values()) / len(scores)
    print(f"Score average is {round(average, 2)}")

    # Dict comprehension 2: only the scores above the average
    high_scores = {k: v for k, v in scores.items() if v > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    ft_data_alchemist()
