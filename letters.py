word="commitment"

favl=input(f"What is your favorite letter in {word}?")

for letter in word:

    if letter.lower() == favl:
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")