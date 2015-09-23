# Get user input
fahrenheit = input("Type a number to convert to Celsius:")

#Convert user input to float
fahrenheit = float(fahrenheit)

#Calculate Celsius
celsius = round((fahrenheit - 32) * 5 /9, 2)

# Convert float to string and give user feedback
print(str(fahrenheit) + " Fahrenheit is " + str(celsius) + " Celsius")