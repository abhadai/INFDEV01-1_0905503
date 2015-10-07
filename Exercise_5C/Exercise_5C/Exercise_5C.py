text = input("Type a text!")
number = input("Type a number (1-26)")
number = int(number)
feedback = ""

for t in text:

    # ORD gets the next ascii character
    new = ord(t) + number

    #Convert ASCII chracter to readable output
    new = chr(new)

    # Append to feedback
    feedback += new

print(feedback)