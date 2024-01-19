kidmeal=(float(input("What is the price of a child's meal?")))
admeal=(float(input("What is the price of an adult's meal?")))
kidamt=(int(input("How many children are there?")))
adamt=(int(input("How many adults are there?")))

subtotal=float((kidmeal*kidamt)+(admeal*adamt))

print(f"Subtotal: ${subtotal:.2f} ")