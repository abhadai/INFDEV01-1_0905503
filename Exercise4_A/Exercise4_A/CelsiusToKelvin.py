# Get user input
celsius = input("Type a number to convert to Kelvin")

# Convert Celsius to Kelvin
kelvin = float(celsius) + 273.15

if kelvin < 0:

# Give user feedback
print(str(celsius) + " Celsius is " + str(kelvin) + " Kelvin") 