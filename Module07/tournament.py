from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_a, strategy_a = opponents[i]
            factory_b, strategy_b = opponents[j]
            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()

            print("* Battle *")
            print(creature_a.describe())
            print(" vs.")
            print(creature_b.describe())
            print(" now fight!")

            try:
                # Both turns are computed before printing anything, so an
                # invalid pairing never leaves a half-played battle.
                turns = strategy_a.act(creature_a) + strategy_b.act(creature_b)
            except InvalidStrategyError as exc:
                print(f"Battle error, aborting tournament: {exc}")
                print()
                return
            for line in turns:
                print(line)
            print()


def run_tournament(
    title: str, entries: list[tuple[str, CreatureFactory, BattleStrategy]]
) -> None:
    labels = []
    for name, _, strategy in entries:
        kind = type(strategy).__name__.removesuffix("Strategy")
        labels.append(f"({name}+{kind})")
    print(title)
    print(f" [ {', '.join(labels)} ]")
    battle([(factory, strategy) for _, factory, strategy in entries])


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    run_tournament(
        "Tournament 0 (basic)",
        [("Flameling", flame, normal), ("Healing", healing, defensive)],
    )
    run_tournament(
        "Tournament 1 (error)",
        [("Flameling", flame, aggressive), ("Healing", healing, defensive)],
    )
    run_tournament(
        "Tournament 2 (multiple)",
        [
            ("Aquabub", aqua, normal),
            ("Healing", healing, defensive),
            ("Transform", transform, aggressive),
        ],
    )


if __name__ == "__main__":
    main()
