# In one of the previous exercises we created the following function that gets
# Celsius degrees as input and returns Fahrenheit, or a message if the Celsius
# input value is less than -273.15.

# Please implement a for  loop that iterates through the following temperatures
# list temperatures=[10,-20,-289,100] and calls the above c_to_f  function in
# each iteration. In other words, this time you are using the function to
# calculate a series of values instead of just one value.

def cel_to_far(c):
    if c < -273.15:
        return "-273.15°C is the lowest temperature in the universe."
    else:
        f = c * 9/5 + 32
        return f

temperatures = [10,-20,-289,100]

for i in temperatures:
    print(cel_to_far(i))
