import sys


def inventory_system() -> dict:
    items = {}

    if len(sys.argv) <= 1:
        print("No valid items")
        return
    for item in sys.argv[1:]:

        if ":" not in item:
            print(f"Error - invalid parameter '{item}'")
            continue
        key, value = item.split(":", 1)
        if len(key) == 0 or len(value) == 0:
            print(f"Error invalid parameter {item} - discarding")
            continue
        if key in items:
            print(f"Redundant item '{key}'")
            continue
        try:
            qty = int(value)
            if qty < 0:
                print(f"Not negative values allowed {qty}")
                continue
            items.update({key: qty})
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
    return items


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    items = inventory_system()
    print(f"Got inventory: {items}")
    print("Item list: ", list(dict.keys(items)))
    total = sum(dict.values(items))
    print(f"Total quantity of the {len(items)} items: {total}")
    for item in items:
        item_per = round((items[item] / total) * 100, 1)
        print(f"Item {item} represents {item_per}%")
    names = list(items.keys())
    max_item = names[0]
    min_item = names[0]
    for name in names:
        if items[name] > items[max_item]:
            max_item = name
        if items[name] < items[min_item]:
            min_item = name
    print(f"Item most abundant: {max_item} with quantity {items[max_item]}")
    print(f"Item least abundant: {min_item} with quantity {items[min_item]}")
    items.update({"magic_item": 1})
    print(items)
