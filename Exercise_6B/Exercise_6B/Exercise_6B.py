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

          if h == 0:
              output += "*"

          if l == 0:
              output += "*"
          
          if h == height - 1:
              output += "*"
print(output)