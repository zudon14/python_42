def validate_ingredients(ingredients: str) -> str:
    # Late import: it runs when the function is called, after both modules
    # are fully loaded, which breaks the circular dependency.
    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    lowered = ingredients.lower()
    found = [item for item in allowed if item in lowered]

    if found:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
