puppies = [
    "Echo 2.5",
    "Evie 8",
    "Finn 3",
    "Gloves 2",
    "Coconut 1",
    "Freddie 4",
]

youngesta=100000

youngestn=0

for line in puppies:

    parts = line.split()

name = parts[0]
age = float(parts[1])

if age < youngesta:
    youngesta = age
    
youngestn = name

print(f"The oldest person is: {youngestn} with an age of {youngesta}")