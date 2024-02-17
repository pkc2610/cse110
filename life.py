high = ["","","",0]
low = ["","","",100]
year_high = ["","","",0]
year_low = ["","","",100]
first = True
tot = 0
num = 0

year = int(input("Enter the year of interest: "))

with open("./life-expectancy.csv") as filething:
    for line in filething:
        if first:
            first = False
        else:
            splat = line.split(',')
            if float(splat[3]) < float(low[3]):
                low = splat
            if float(splat[3]) > float(high[3]):
                high = splat
            if int(splat[2]) == int(year):
                num += 1
                tot += float(splat[3])
                if float(splat[3]) < float(year_low[3]):
                    year_low = splat
                if float(splat[3]) > float(year_high[3]):
                    year_high = splat

print(f"The overall max life expectancy is: {float(high[3]):.2f} from {high[2]} in {high[0]}")
print(f"The overall min life expectancy is: {float(low[3]):.2f} from {low[2]} in {low[0]}")
print(f"For the year {year}:")
print(f"The average life expectancy across all countries was {(tot / num):.2f}")
print(f"The max life expectancy was in {year_high[0]} with {float(year_high[3])}")
print(f"The min life expectancy was in {year_low[0]} with {float(year_low[3])}")