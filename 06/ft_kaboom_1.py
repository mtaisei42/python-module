import alchemy.grimoire.dark_spellbook


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Using grimoire module directly")
    result = alchemy.grimoire.dark_spellbook.dark_spell_record("Fantasy", "Earth, wind and fire")
    print(f"esting record dark spell: {result}")



if __name__ == "__main__":
    main()
