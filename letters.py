word="commitment"

favl=input(f"What is your favorite letter in {word}?")

for let in word:

    if let.lower() == favl:
        print(let.upper(), end="")
    else:
        print(let.lower(), end="")

for let in word:

    if let.lower() == let.lower():
        print("_", end="")
    else:
        print(let.lower(), end="")