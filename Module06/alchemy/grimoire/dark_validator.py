from alchemy.grimoire.dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    lowered = ingredients.lower()
    found = [item for item in allowed if item in lowered]

    if found:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"