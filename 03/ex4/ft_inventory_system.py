import sys


def parse_inventory_argv() -> dict[str, int]:
    inventory = {}
    for arg in sys.argv[1:]:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item, count_str = arg.split(':')
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
    items = dict.keys(inventory)
    count = dict.values(inventory)
    total_count = sum(count)
    print(f"Item list: {items}")
    print(f"Total puantity of the {len(items)} item: {total_count}")
    for item in inventory:
        print(f"Item {item} represents"
              f"{round(inventory[item] / total_count * 100, 1)}%")
    most_item = max(inventory, key=inventory.get)
    least_item = min(inventory, key=inventory.get)
    print(f"Item most abundant: {most_item}"
          f"with quantity {inventory[most_item]}")
    print(f"Item least abundant: {least_item}"
          f"with quantity {inventory[least_item]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
