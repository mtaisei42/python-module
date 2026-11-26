from ex3 import TransformCreatureFactory


def main() -> None:
    factory = TransformCreatureFactory()
    print("Testing Creature with transform capability")
    creatures = (
        ("base", factory.create_base()),
        ("evolved", factory.create_evolved()),
    )
    for stage, creature in creatures:
        print(f"{stage}:")
        print(creature.describe())
        print(creature.attack())
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


if __name__ == "__main__":
    main()
