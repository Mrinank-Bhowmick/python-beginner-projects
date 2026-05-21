# === Fantasy Game Inventory · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @ibra-kdbra.

# Print each item and count in inventory
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0

    # Loop over every item and add to total
    for k, v in inventory.items():
        print(v, " ", k)
        item_total += v

    print("Total number of items: " + str(item_total))


# Add a list of new items to the inventory dict
def addToInventory(inventory, addedItems):
    updatedInventory = dict(inventory)
    # Count each item from the loot list
    for item in addedItems:
        updatedInventory.setdefault(item, 0)
        updatedInventory[item] += 1

    return updatedInventory


if __name__ == "__main__":

    # Show an existing inventory
    stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
    displayInventory(stuff)

    # Add dragon loot to a smaller inventory and display
    inv = {"gold coin": 42, "rope": 1}
    dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)
