def cel_to_far(c):
    if c < -273.15:
        return "-273.15°C is the lowest temperature in the universe."
    else:
        f = c * 9/5 + 32
        return f

degree = float(input("Celsius to Fahrenheit: "))
print(cel_to_far(degree))
