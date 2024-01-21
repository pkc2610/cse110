kidmeal=(float(input("What is the price of a child's meal?")))
admeal=(float(input("What is the price of an adult's meal?")))
kidamt=(int(input("How many children are there?")))
adamt=(int(input("How many adults are there?")))

subtotal=float((kidmeal*kidamt)+(admeal*adamt))

print(f"Subtotal: ${subtotal:.2f} ")

rate=float(input("What is the sales tax rate? (as a percentage of total cost)"))

total_sales_tax=rate*subtotal
total=total_sales_tax + subtotal

amount=float(input("What will be your payment amount?"))

change=amount-total

print(f"Your change is ${change:.2f}")

print(" ")

print("Thank you for coming!")