import sys


def parse_inventory_argv() -> dict[str, int]:
    inventory = {}
    for arg in sys.argv[1:]:
        if arg.count(':') != 1:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item, count_str = arg.split(':')
        if not item.strip():
            print(f"Error - invalid parameter '{arg}'")
            continue
        try:
            if item in inventory:
                print(f"Redundant item '{item}' - discarding")
                continue
            inventory[item] = int(count_str)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory_argv()
    print(f"Got inventory: {inventory}")
    items = list(inventory.keys())
    count = dict.values(inventory)
    total_count = sum(count)
    print(f"Item list: {items}")
    print(f"Total quantity of the {len(items)} items: {total_count}")
    for item in inventory:
        if total_count == 0:
            print(f"Item {item} represents N/A (total quantity is zero)")
        else:
            print(f"Item {item} represents "
                  f"{round(inventory[item] / total_count * 100, 1)}%")
    if inventory:
        most_item = max(inventory, key=inventory.__getitem__)
        least_item = min(inventory, key=inventory.__getitem__)
        print(f"Item most abundant: {most_item} "
              f"with quantity {inventory[most_item]}")
        print(f"Item least abundant: {least_item} "
              f"with quantity {inventory[least_item]}")
    else:
        print("No items in inventory.")

    new_item = "magic_item"
    suffix = 1
    while new_item in inventory:
        new_item = f"magic_item_{suffix}"
        suffix += 1
    inventory.update({new_item: 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
