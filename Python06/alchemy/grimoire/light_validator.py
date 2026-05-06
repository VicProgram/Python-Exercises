from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:

    allowed = light_spell_allowed_ingredients()
    ing_lower = ingredients.lower()

    is_valid = any(item for item in allowed if item in ing_lower)

    if is_valid:
        status = "VALID"
    else:
        status = "INVALID"

    return (f"({ingredients} - {status})")
