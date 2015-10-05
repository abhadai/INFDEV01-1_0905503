# Get user input
height = input("Type the number of asteriks you want for the height")
length = input("Type the number of asteriks you want for the length")

# Convert string to int
height = int(height)
length = int(length)
output = ""

for h in range(0, height):
      output += "\n"
      for l in range(0, length):
          output += "*"       

print(output)