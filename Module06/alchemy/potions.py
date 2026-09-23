from elements import create_fire, create_water  # absolute: root elements.py
from .elements import create_air, create_earth  # relative: alchemy/elements.py


def healing_potion() -> str:
    return (
        f"Healing potion brewed with '{create_earth()}' "
        f"and '{create_air()}'"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with '{create_fire()}' "
        f"and '{create_water()}'"
    )
