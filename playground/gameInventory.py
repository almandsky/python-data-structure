stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print('Inventory')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total += int(v)

    print("\nTotal number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inv_item = inventory.get(item, 0);
        if item in inventory:
            inventory[item] = inv_item + 1
        else:
            inventory[item] = 1

displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(stuff, dragonLoot)
displayInventory(stuff)
