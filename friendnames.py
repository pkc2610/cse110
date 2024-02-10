friends = []

names = None

while names != "end":
    names = input("Type the name of one of your friends: ")
    if names != "end":
        friends.append(names)

print()
print("Your friends are:")