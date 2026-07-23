from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    user_ingredients = ingredients.replace(","," ").split()
    is_valid = any(item in allowed for item in user_ingredients)

    if is_valid:
        return f"({ingredients} - VALID)"
    else:
        return f"({ingredients} -> INVALID)"
