with open("hr_system.txt") as f:
    for line in f:
        parts=line.split(" ")

name = parts[0]
id = parts[1]
title = parts[2]
salary = parts[3]

print(f"Name: {name}, ID: {id}, Title: {title}, Salary: {salary}")