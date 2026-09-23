import random

ALL_ACHIEVEMENTS: list[str] = [
    "First Steps",
    "Boss Slayer",
    "Master Explorer",
    "Collector Supreme",
    "Treasure Hunter",
    "Strategist",
    "Untouchable",
    "Speed Runner",
    "Hidden Path Finder",
    "Crafting Genius",
    "World Savior",
    "Survivor",
    "Unstoppable",
    "Sharp Mind",
    "Dragon Tamer",
    "Night Owl",
    "Lucky Strike",
    "Iron Will",
    "Silent Hunter",
    "Perfect Aim",
    "Deep Diver",
    "Sky Walker",
    "Time Bender",
    "Ghost Whisperer",
    "Legendary Smith",
    "Chest Cracker",
    "Combo Master",
    "Pacifist",
    "Marathoner",
    "Quest Finisher",
]


def gen_player_achievements() -> set[str]:
    amount = random.randint(8, 22)
    return set(random.sample(ALL_ACHIEVEMENTS, amount))


def elements_common(*players: set[str]) -> set[str]:
    return set.intersection(*players)


if __name__ == "__main__":
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    everything = set(ALL_ACHIEVEMENTS)

    all_distinct = alice.union(bob, charlie, dylan)
    common = elements_common(alice, bob, charlie, dylan)

    only_alice = alice.difference(bob, charlie, dylan)
    only_bob = bob.difference(alice, charlie, dylan)
    only_charlie = charlie.difference(alice, bob, dylan)
    only_dylan = dylan.difference(alice, bob, charlie)

    missing_alice = everything.difference(alice)
    missing_bob = everything.difference(bob)
    missing_charlie = everything.difference(charlie)
    missing_dylan = everything.difference(dylan)

    print("=== Achievement Tracker System ===\n")

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")

    print(f"All distinct achievements: {all_distinct}\n")
    print(f"Common achievements: {common}\n")

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}\n")

    print(f"Alice is missing: {missing_alice}")
    print(f"Bob is missing: {missing_bob}")
    print(f"Charlie is missing: {missing_charlie}")
    print(f"Dylan is missing: {missing_dylan}")
