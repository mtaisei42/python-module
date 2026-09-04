import ex0, ex1, ex2
from ex2.strategy import InvalidStrategyError

def battle(creature_strategys: list):

    print("*** Tournament ***")
    total = len(creature_strategys)
    print(f"{len(creature_strategys)} opponents involved")

    for i in range(total):
        for j in range(i + 1, total):
            creature1, strategy1 = creature_strategys[i]
            creature2, strategy2 = creature_strategys[j]
            print("\n* Battle *")
            creature1.describe()
            print(" .vs")
            creature2.describe()
            print(" .now fight")
            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except InvalidStrategyError as e:
                print(e)

def main() -> None:

    aquafactory = ex0.AquaFactory()
    flamefactory = ex0.FlameFactory()
    heelfactory = ex1.HeelingCreatureFactory()
    transformfactory = ex1.TransformCreatureFactory()
    normal = ex2.NormalStrategy()
    aggressive = ex2.AggressiveStrategy()
    defensive = ex2.DefensiveStrategy()


    Aquabub = aquafactory.create_base()
    Flameling = flamefactory.create_base()
    Sproutling = heelfactory.create_base()
    Shiftling = transformfactory.create_base()

    buttle1 = [(Flameling, normal), (Sproutling, defensive)]
    buttle2 = [(Flameling, aggressive), (Sproutling, defensive)]
    buttle3 = [(Aquabub, normal), (Sproutling, defensive), (Shiftling, aggressive)]


    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle(buttle1)

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(buttle2)

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(buttle3)



if __name__ == "__main__":
    main()
