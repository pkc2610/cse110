print("Please enter the items of the shopping list (type: quit to finish):")

shoppinglist = []
item = None

while item != "end":
    item = input("Item: ")

    if item != "end":
        shoppinglist.append(item)