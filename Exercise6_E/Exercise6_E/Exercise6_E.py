import math

# Get user input
diameter = int(input("Write a number for the width of your circle!"))

# Radius = diameter / 2
r = diameter / 2
output = ""

for i in range(0, diameter):

    # Calculate the first middle
    m1 = (i - (r)) * (i - (r))

    for j in range(0, diameter):

        # Calculate second middle
        m2 = (j - (r)) * (j - (r))

        # If both middles are smaller than the radius, print and hashtag
        if math.sqrt(m1 + m2) < r:
            output += "#"
        else:
            output += " "
    output += "\n"

print(output)