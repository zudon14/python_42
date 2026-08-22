
from random import randint


def ft_data_alchemist() -> None:
    print("=== Game Data Alchemist ===")

    # Lista inicial
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

    # List comprehension 1: todos capitalizados
    all_capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized}")

    # List comprehension 2: apenas os que já eram capitalizados
    capitalized_only = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {capitalized_only}")

    # Dict comprehension 1: criar dicionário de scores
    score_dict = {name: randint(0, 1000) for name in all_capitalized}
    print(f"Score dict: {score_dict}")

    # Média dos scores
    average = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {average}")

    # Dict comprehension 2: apenas scores acima da média
    high_scores = {
        name: score
        for name, score in score_dict.items()
        if score > average
    }

    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    ft_data_alchemist()