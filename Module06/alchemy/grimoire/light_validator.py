def validate_ingredients(ingredients: str) -> str:
    from alchemy.grimoire.light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    lowered = ingredients.lower()
    found = [item for item in allowed if item in lowered]

    if found:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"