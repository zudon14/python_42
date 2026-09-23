from elements import create_fire  # absolute: root elements.py
from alchemy.potions import strength_potion  # absolute: from the top package
from ..elements import create_air  # relative: alchemy/elements.py


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}' "
        f"and '{strength_potion()}' mixed with '{create_fire()}'"
    )
