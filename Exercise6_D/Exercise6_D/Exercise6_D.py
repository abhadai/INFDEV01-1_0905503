number = input("Enter a number for the maximum length the triangle should have!")
number = int(number)
spaces = number -1
output = ""

for i in range(0, number):
    for j in range(0, spaces):
        output += " " 
    for k in range(0, number - spaces):
        output += "* "
    
    output += "\n"
    spaces -= 1

print(output)