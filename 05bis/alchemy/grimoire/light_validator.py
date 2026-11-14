def validate_ingredients(ingredients: str) -> str:

    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    user_ingredients = ingredients.lower().replace(",", " ").split()
    is_valid = any(item in allowed for item in user_ingredients)

    if is_valid:
        status = "VALID"

    else:
        status = "INVALID"

    return f"({ingredients} - {status})"
