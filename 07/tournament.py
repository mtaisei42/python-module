import ex0, ex1, ex2
from ex2.strategy import InvalidStrategyError

def battle(creature_strategys: list):

    print("*** Tournament ***")
    total = len(creature_strategys)
    print(f"{len(creature_strategys)} opponents involved")

    for i in range(total - 1):
        print("\n* Battle *")
        creature_strategys[i][0].describe()
        print(" .vs")
        for j in range(total - 1):
            creature_strategys[j+1][0].describe()
            print(" now fight!")
            try:
                creature_strategys[i][1].act(creature_strategys[i][0])
            except InvalidStrategyError as e:
                print(e)
                return
            try:
                creature_strategys[j+1][1].act(creature_strategys[j+1][0])
            except InvalidStrategyError as e:
                print(e)
                return
    

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
