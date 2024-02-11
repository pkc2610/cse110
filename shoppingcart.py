print("Welcome to the Shopping Cart Program!")
print()
print("Please select one of the following: \n 1. Add item \n 2. View cart \n 3. Remove item \n 4. Compute total \n 5. Quit")

shoppinglist = []
item = None

action=int(input("Please select an action: "))
    
while action != 5:

    if action == 1:
     item=input("What item would you like to add? ")
     shoppinglist.append(item)
     action += 4

    elif action == 2:
       #could maybe put a for loop in here if I'm really feeling smort--minute marker 6:15 of the first video 
       print(f"{shoppinglist}")
       action += 3

    elif action ==3:
       info=input("What item would you like to remove? ")
       shoppinglist.pop(info)
       action += 2
    
    elif action == 4:
       print("Process incoming ")
       action += 1