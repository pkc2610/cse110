word="flavortown"
guess = input("What is your guess?")
guesses=1

print("Welcome to the word guessing game!!")
print()
print("You'll need to write in 10-letter words until you guess the correct 10-letter word!")
print()
print("Just a heads up--this program does NOT account for duplicates. For example, if you \nenter the word 'food' and the answer is 'rose,' then the hint would show as '_Oo_,' \ndespite there only being one 'o' in 'rose.'")
print()
print("Best of luck!!")


while len(guess) != len(word):
    print("Your guess was not correct")
    guess=input("What is your guess?")
    guesses=guesses+1


guess = guess.lower()

    
print("You got it!!")
print(f"It took you {guesses} guesses")