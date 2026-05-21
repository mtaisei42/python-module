def ft_seed_inventory(seed: str, quant: int, unit: str) -> None:
    if unit == "packets":
        print(seed.capitalize(), "seed:", quant, unit, "available")
    elif unit == "grams":
        print(seed.capitalize(), "seed:", quant, unit, "total")
    elif unit == "area":
        print(seed.capitalize(), "seed:", "covers", quant, "square meters")
    else:
        print("Unknown unit type")


ft_seed_inventory("tomato", 15, "packets")
ft_seed_inventory("carrot", 8, "grams")
ft_seed_inventory("lettuce", 12, "area")
