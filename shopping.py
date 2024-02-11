print("Please enter the items of the shopping list (type: quit to finish):")

shoppinglist = []
item = None

while item != "end":
    item = input("Item: ")

    if item != "end":
        shoppinglist.append(item)

print("\nThe shopping list is:")
for item in shoppinglist:
    print(item)


print("\nThe shopping list with indexes is:")
for i in range(len(shoppinglist)):
    item = shoppinglist[i]
    print(f"{i}. {item}")