with open("hr_system.txt") as f:
    for line in f:
        parts=line.split(" ")

name = parts[1]
title = parts[3]

print(f"Name: {name}, Title: {title}")