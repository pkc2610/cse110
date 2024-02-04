word="flavortown"
guesses=1

print("Welcome to the word guessing game!!")
print()
print("Just a heads up--this program does NOT account for duplicates. For example, if you \nenter the word 'food' and the answer is 'rose,' then the hint would show as '_Oo_,' \ndespite there only being one 'o' in 'rose.'")
print()
print("Best of luck!!")

guess=input("What is your guess?")
while len(guess) != len(word):
    print("Your guess was not correct")
    guess=input("Try again!")
    guesses=guesses+1


guess = guess.lower()

while word != guess:

    thing = ""

    for i in range(len(word)):
        if word[i] == guess[i]:
            thing = thing + guess[i].upper()
        elif word.__contains__(guess[i]):
            thing = thing + guess[i].lower()
        else:
            thing = thing + '_'

    print(f"Your guess is {thing}")
    guess=input("Try again!")
    guess = guess.lower()

    guesses=guesses+1
print("You got it!!")
print(f"It took you {guesses} guesses")