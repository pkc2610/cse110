def getWindChill(wind, t):
    v = wind ** 0.16
    return 35.74 + (0.6215 * t) - (35.75 * v) + (0.4275 * t * v)

def getFarFromCel(cel):
    return (cel * (9/5)) + 32

temp = float(input("What is the temperature? "))
deg = input("Fahrenheit or Celsius (F/C)? ")

if (deg.lower() == "c"):
    temp = getFarFromCel(temp)

for i in range(5,65,5):
    print(f"At temperature {temp}F, and wind speed {i} mph, the windchill is: {getWindChill(i, temp):.2f}F")