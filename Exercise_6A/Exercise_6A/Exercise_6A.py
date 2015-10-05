height = input("Type the number of asteriks you want for the height")
length = input("Type the number of asteriks you want for the length")
output = ""

for h in range(0, int(height)):
      output += "\n"
      for l in range(0, int(length)):
         output += "*"

print(output)