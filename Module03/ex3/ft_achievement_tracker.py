from random import sample, randint


def gen_player_achievements(achievements: list[str]) -> set[str]:
    amount = randint(4, len(achievements))
    return set(sample(achievements, amount))


def elements_common(*players: set[str]) -> set[str]:
    return set.intersection(*players)


if __name__ == "__main__":

    achievements = [
        "First Steps",
        "Boss Slayer",
        "Master Explorer",
        "Collector Supreme",
        "Treasure Hunter",
        "Strategist",
        "Untouchable",
        "Speed Runner",
        "Hidden Path Finder"
    ]

    alice = gen_player_achievements(achievements)
    bob = gen_player_achievements(achievements)
    charlie = gen_player_achievements(achievements)
    dylan = gen_player_achievements(achievements)

    all_distinct = set.union(alice, bob, charlie, dylan)
    common = elements_common(alice, bob, charlie, dylan)

    only_alice = alice.difference(set.union(bob, charlie, dylan))
    only_bob = bob.difference(set.union(alice, charlie, dylan))
    only_charlie = charlie.difference(set.union(alice, bob, dylan))
    only_dylan = dylan.difference(set.union(alice, bob, charlie))

    missing_alice = all_distinct.difference(alice)
    missing_bob = all_distinct.difference(bob)
    missing_charlie = all_distinct.difference(charlie)
    missing_dylan = all_distinct.difference(dylan)

    print("=== Achievement Tracker System ===\n")

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")

    print(f"All distinct achievements: {all_distinct}")
    print(f"Common achievements: {common}\n")

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}\n")

    print(f"Alice is missing: {missing_alice}")
    print(f"Bob is missing: {missing_bob}")
    print(f"Charlie is missing: {missing_charlie}")
    print(f"Dylan is missing: {missing_dylan}")