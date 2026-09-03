import ex0

def battle(creature1, creature2):

    creature1.describe()
    print(" vs.")
    creature2.describe()

    print(" fight!")
    creature1.attack()
    creature2.attack()


def main() -> None:

    flame_fact = ex0.FlameFactory()
    aqua_fact = ex0.AquaFactory()

    Flameling = flame_fact.create_base()
    Pyrodon = flame_fact.create_evolved()
    Aquabub = aqua_fact.create_base()
    Torragon = aqua_fact.create_evolved()

    print("Testing factory")
    Flameling.describe()
    Flameling.attack()
    Pyrodon.describe()
    Pyrodon.attack()

    print("\nTesting factory\n")
    Aquabub.describe()
    Aquabub.attack()
    Torragon.describe()
    Torragon.attack()

    print("Testing battle")
    battle(Flameling,   Aquabub)




main()
