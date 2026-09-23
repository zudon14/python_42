from ex0 import CreatureFactory
from ex0.creature import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.heal_capability import HealCapability
from ex1.transform_capability import TransformCapability


def test_healing(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    stages: list[tuple[str, Creature]] = [
        (" base:", factory.create_base()),
        (" evolved:", factory.create_evolved()),
    ]
    for label, creature in stages:
        print(label)
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())
        else:
            print(f"{creature.name} has no healing capability")
    print()


def test_transform(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    stages: list[tuple[str, Creature]] = [
        (" base:", factory.create_base()),
        (" evolved:", factory.create_evolved()),
    ]
    for label, creature in stages:
        print(label)
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            print(f"{creature.name} has no transform capability")


def main() -> None:
    try:
        test_healing(HealingCreatureFactory())
        test_transform(TransformCreatureFactory())
    except NotImplementedError as exc:
        print(f"Capability error: {exc}")


if __name__ == "__main__":
    main()
