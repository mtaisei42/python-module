from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    for creature in (factory.create_base(), factory.create_evolved()):
        print(creature.describe())
        print(creature.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()
    print("Testing battle")
    print(creature1.describe())
    print("vs.")
    print(creature2.describe())
    print("fight!")
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()
    test_factory(flame_factory)
    print()
    test_factory(transform_factory)
    print()
    battle(flame_factory, transform_factory)


if __name__ == "__main__":
    main()
