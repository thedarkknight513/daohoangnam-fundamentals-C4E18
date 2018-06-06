inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory["pocket"] = ["Seasheel", "strange berry", "flint"]
location = inventory["backpack"].index("dagger")
del inventory["backpack"][location]
gold_to_add = int(input("How much gold do you want to add"))
inventory["gold"] += gold_to_add


print(inventory)

