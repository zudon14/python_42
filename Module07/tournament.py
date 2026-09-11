from itertools import combinations

from ex0 import CreatureFactory
from ex2 import BattleStrategy, InvalidStrategyError

Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    for (factory_a, strategy_a), (factory_b, strategy_b) in combinations(opponents, 2):
        creature_a = factory_a.create_base()
        creature_b = factory_b.create_base()

        print("* Battle *")
        print(creature_a.describe())
        print(" vs.")
        print(creature_b.describe())
        print(" now fight!")

        try:
            for line in strategy_a.act(creature_a):
                print(line)
            for line in strategy_b.act(creature_b):
                print(line)
        except InvalidStrategyError as exc:
            print(f"Battle error, aborting tournament: {exc}")
            return
        print()