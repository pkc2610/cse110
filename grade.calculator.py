percent = int(input("What is your grade percent? "))
if percent >= 90:
    letter = "A"
if percent >= 80:
    letter = "B"
if percent >= 70:
    letter = "C"
if percent >= 60:
    letter = "D"
else: letter = "F"

print(f"Your letter grade is: {letter}")

if percent > 70:
    print("Congratulations! You passed the class!")
else: print("Stay focused and you'll get it next time!")