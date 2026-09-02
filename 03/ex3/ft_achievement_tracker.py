import random


All_achiev = ["Strategist", "Speed Runner", "Unstoppable",
                "Untouchable", "Boss Slayer",
                "Crafting Genius", "World Savior", "Survivor", "Master Explorer",
                "Treasure Hunter","Hidden Path Finder", "First Steps",
                "Collector Supreme", "Sharp Mind"]


def gen_player_achievements() -> set[str]:
    count = random.randint(5, 10)
    selected_achiev = set(random.sample(All_achiev, count))
    return selected_achiev


def main() -> None:
    Achievements = []
    for _ in range(4):
        Achievements.append(gen_player_achievements())

    Alice = Achievements[0]
    Bob = Achievements[1]
    Charlie = Achievements[2]
    Dylan = Achievements[3]

    print("=== Achievement Tracker System ===\n")
    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}")

    All_distinct = set.union(Alice,Bob, Charlie, Dylan)
    print(f"\nAll distinct achievements: {All_distinct}")
    Comon = set.intersection(Alice, Bob, Charlie, Dylan)
    print(f"\nCommon achievements: {Comon}\n")

    only_Alice = Alice.difference(Bob, Charlie, Dylan)
    only_Bob = Bob.difference(Alice, Charlie, Dylan)
    only_Charlie = Charlie.difference(Bob, Alice, Dylan)
    only_Dylan = Dylan.difference(Bob, Charlie, Alice)
    print(f"Only Alice has: {only_Alice}")
    print(f"Only Bob has: {only_Bob}")
    print(f"Only Charlie has: {only_Charlie}")
    print(f"Only Dylan has: {only_Dylan}")
    print()
    miss_Alice = set(All_achiev).difference(Alice)
    miss_Bob = set(All_achiev).difference(Bob)
    miss_Charlie = set(All_achiev).difference(Charlie)
    miss_Dylan = set(All_achiev).difference(Dylan)
    print(f"Alice is missing: {miss_Alice}")
    print(f"Bob is missing: {miss_Bob}")
    print(f"Charlie is missing: {miss_Charlie}")
    print(f"Dylan is missing: {miss_Dylan}")

if __name__ == "__main__":
    main()
