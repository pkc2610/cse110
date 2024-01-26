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