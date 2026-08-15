
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:

    string = seed_type.capitalize()

    if unit == "packets":
        print(string + " seeds: " + str(quantity) + " packets available")
    elif unit == "grams":
        print(string + " seeds: " + str(quantity) + " grams total")
    elif unit == "area":
        print(string + " seeds: " + "covers " + str(quantity) + " square meters")
    else:
        print("Unknown unit type")
    