import sys


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}

    # Parse "<item_name>:<quantity>" parameters
    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item, raw_quantity = arg.split(":", 1)
        item = item.strip()

        if not item:
            print(f"Error - invalid parameter '{arg}'")
            continue

        try:
            quantity = int(raw_quantity.strip())
        except ValueError as err:
            print(f"Quantity error for '{item}': {err}")
            continue

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        inventory[item] = quantity

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    if total > 0:
        for item in item_list:
            percent = round(inventory[item] / total * 100, 1)
            print(f"Item {item} represents {percent}%")

    # Most / least abundant (first one wins in case of a tie)
    if item_list:
        most = item_list[0]
        least = item_list[0]

        for item in item_list:
            if inventory[item] > inventory[most]:
                most = item
            if inventory[item] < inventory[least]:
                least = item

        print(f"Item most abundant: {most} with quantity {inventory[most]}")
        print(f"Item least abundant: {least} with quantity {inventory[least]}")

    # Add a new item
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system()
