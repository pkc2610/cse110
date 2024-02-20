print("Welcome to the Shopping Cart Program!")
print()

shoppinglist = []
listprices = []
item = None
action = 0
    
while action != 5:
    print("Please select one of the following: \n 1. Add item \n 2. View cart \n 3. Remove item \n 4. Compute total \n 5. Quit")
    action=int(input("Please select an action: "))

    if action == 1:
     item=input("What item would you like to add? ")
     itemprice=float(input(f"What is the price of {item}? "))
     shoppinglist.append(item)
     listprices.append(itemprice)
     print(f"{item} has been added to your cart.")

    elif action == 2:
       #could maybe put a for loop in here if I'm really feeling smort--minute marker 6:15 of the first video 
         print("The contents of the shopping cart are:")
         for i in range(len(shoppinglist)):
            print(f"{i+1}: {shoppinglist[i]} - ${listprices[i]}")

    elif action ==3:
       info=int(input("What item would you like to remove? "))
       if info >= len(shoppinglist) or info < 0:
          print("Sorry, that is not a valid item number.")
       else:
          del shoppinglist[int(info) - 1]
          del listprices[int(info) - 1]
    
    elif action == 4:
       total = 0.0
       for i in listprices:
          total += i
       print(f"The total price of the items in the shopping cart is ${total:.2f}")
    print()
print("Thank you! Goodbye.")
