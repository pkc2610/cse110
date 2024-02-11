print("Welcome to the Shopping Cart Program!")
print()
print("Please select one of the following: \n 1. Add item \n 2. View cart \n 3. Remove item \n 4. Compute total \n 5. Quit")

shoppinglist = []
item = None

action=int(input("Please select an action: "))
    
while action != 5:
    
    if action == 1:
     item=input("What item would you like to add?")
     shoppinglist.append(item)

    elif action == 2:
       print(f"{shoppinglist}")

    elif action ==3:
       info=input("What item would you like to remove?")
       shoppinglist.append(info)
    
    elif action == 4:
       print("Process incoming")