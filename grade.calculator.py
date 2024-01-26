percent = int(input("What is your grade percent? "))
if percent >= 90:
    letter = "A"
elif percent >= 80:
    letter = "B"
elif percent >= 70:
    letter = "C"
elif percent >= 60:
    letter = "D"
else: letter = "F"

print(f"Your letter grade is: {letter}")

if percent > 70:
    print("Congratulations! You passed the class!")
else: print("Stay focused and you'll get it next time!")