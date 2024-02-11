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
         for i in range(len(shoppinglist)):
            print(f"{shoppinglist[i]}: ${listprices[i]}")
         action=int(input("Please select an action: "))

    elif action ==3:
       info=input("What item would you like to remove? ")
       index = shoppinglist.index(info)
       shoppinglist.pop(index)
       listprices.pop(index)
       action=int(input("Please select an action: "))
    
    elif action == 4:
       total = 0.0
       for i in listprices:
          total += i
       print(f"Your total is: {total}")
       action=int(input("Please select an action: "))