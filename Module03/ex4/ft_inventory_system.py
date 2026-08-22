
import sys


def ft_inventory_system() -> None:
    argv = sys.argv[1:]
    inventory = {}

    # Construção do inventário
    for arg in argv:

        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item, qty = arg.split(":", 1)
        item = item.strip()

        try:
            qty = int(qty.strip())
        except ValueError:
            print(f"Quantity error for '{item}'")
            continue

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        inventory[item] = qty

    print("=== Inventory System Analysis ===")

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    if total > 0:
        for item in inventory.keys():
            percent = round((inventory[item] / total) * 100, 1)
            print(f"Item {item} represents {percent}%")

    # Item mais abundante
    keys = list(inventory.keys())

    if keys:
        max_item = keys[0]
        min_item = keys[0]

        for item in keys:
            if inventory[item] > inventory[max_item]:
                max_item = item
            if inventory[item] < inventory[min_item]:
                min_item = item

        print(
            f"Item most abundant: {max_item} "
            f"with quantity {inventory[max_item]}"
        )

        print(
            f"Item least abundant: {min_item} "
            f"with quantity {inventory[min_item]}"
        )

    # Adiciona novo item
    inventory.update({"magic_item": 1})

    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system()  