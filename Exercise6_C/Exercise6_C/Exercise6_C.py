# Triangles

number = input("Enter the maximal length of asteriks you want to use to draw a triangle!")
number = int(number)

# First row has number - 1 spaces
spaces = number -1
output = ""

# Loop through max number
for i in range (0, number):

    # Put number of spaces at the end
    for j in range (0, number - spaces):
        output += "*"

    output += "\n"
    spaces -= 1
0


print(output)