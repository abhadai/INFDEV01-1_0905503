character = input("Type a character (A-Z)")
number = input("Type a number (0-26)")
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = list(alphabet)
i = 0

print(number)

for a in alphabet:
    i += 1

    if i == number:
        a -= number
        print(alphabet[a])