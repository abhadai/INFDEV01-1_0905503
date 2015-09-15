number = int(input("Enter a number"))
stars = ""

# Iterate the given number of times
for i in range (0, number):
    
    endLine = "*"
    rowLine = ""
    
    for i in range(0, i):
        rowLine += "*"
        print(rowLine + endLine)

print(stars)