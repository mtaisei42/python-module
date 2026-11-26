from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (
    AggressiveStrategy,
    BattleStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]
            creature1 = factory1.create_base()
            creature2 = factory2.create_base()
            print("\n* Battle *")
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")
            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


def main() -> None:
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Shiftling+Aggressive) ]")
    battle([(flame_factory, normal), (transform_factory, aggressive)])

    print("\nTournament 1 (error)")
    print("[ (Shiftling+Aggressive), (Flameling+Aggressive) ]")
    battle([(transform_factory, aggressive), (flame_factory, aggressive)])

    print("\nTournament 2 (multiple)")
    print("[ (Flameling+Normal), (Shiftling+Aggressive), (Shiftling+Normal) ]")
    battle([
        (flame_factory, normal),
        (transform_factory, aggressive),
        (transform_factory, normal),
    ])


if __name__ == "__main__":
    main()
