from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    base = factory.create_base()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())
    # ... repete para create_evolved()


def test_transform(factory: TransformCreatureFactory) -> None:
    ...  # describe, attack, transform, attack de novo, revert


def main() -> None:
    test_healing(HealingCreatureFactory())
    test_transform(TransformCreatureFactory())


if __name__ == "__main__":
    main()