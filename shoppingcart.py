#Store prices as well as names. DONE
#Change the add functionality to also ask for and store the price of the item. DONE
#Change the display functionality to also display the prices of the items. DONE
#When displaying the items, display a number in front of each item. The numbers should start with 1.
#Complete the option to display the total amount of the prices of all the items in the shopping cart.
#Whenever prices are displayed, they should be shown to two decimal places and include the appropriate currency symbol (for example $, €, etc.)
#Complete the option to remove an item from the shopping cart.
#When removing an item, you should verify the following:
#Both the item name and price are removed from their respective lists.
#The number the user enters should be converted to a 0-based index and checked to make sure it is within the bounds of the list.
#The program allows you to remove any item from the list including the first one and the last one. (Sometimes, if you have a bug in your project you might not allow removing the last item as you should.)



print("Welcome to the Shopping Cart Program!")
print()
print("Please select one of the following: \n 1. Add item \n 2. View cart \n 3. Remove item \n 4. Compute total \n 5. Quit")

shoppinglist = []
listprices = []
item = None

action=int(input("Please select an action: "))
    
while action != 5:

    if action == 1:
     item=input("What item would you like to add? ")
     itemprice=float(input(f"What is the price of {item}? "))
     shoppinglist.append(item)
     listprices.append(itemprice)

     action=int(input("Please select an action: "))

    elif action == 2:
       #could maybe put a for loop in here if I'm really feeling smort--minute marker 6:15 of the first video 
         print("The shopping list and prices are: ")
         print(f"{shoppinglist}")
         print(f"{listprices}")
         action=int(input("Please select an action: "))

    elif action ==3:
       info=input("What item would you like to remove? ")
       shoppinglist.pop(info)
       action=int(input("Please select an action: "))
    
    elif action == 4:
       print("Process incoming ")
       action=int(input("Please select an action: "))