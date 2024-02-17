high = 0
low = 100
first = True

with open("./life-expectancy.csv") as filething:
    for line in filething:
        if first:
            first = False
        else:
            splat = line.split(',')
            if float(splat[3]) < low:
                low = float(splat[3])
            if float(splat[3]) > high:
                high = float(splat[3])

print(f"The highest life expectancy was: {high} the lowest life expectancy was {low}")