import ex1

def main():

    heelfactory = ex1.HeelingCreatureFactory()
    transformfactory = ex1.TransformCreatureFactory()
    Sproutling = heelfactory.create_base()
    Bloomelle = heelfactory.create_evolved()
    Shiftling = transformfactory.create_base()
    Morphagon = transformfactory.create_evolved()

    print("Testing Creature with healing capability")
    print(" base:")
    Sproutling.describe()
    Sproutling.attack()
    Sproutling.HealCapability("itself")

    print(" evolved:")
    Bloomelle.describe()
    Bloomelle.attack()
    Bloomelle.HealCapability("itself")

    print("Testing Creature with transform capability")
    print(" base:")
    Shiftling.describe()
    Shiftling.attack()
    Shiftling.transform()
    Shiftling.attack()
    Shiftling.revert()

    print(" evolved:")
    Morphagon.describe()
    Morphagon.attack()
    Morphagon.transform()
    Morphagon.attack()
    Morphagon.revert()

main()
