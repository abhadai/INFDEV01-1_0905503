password = input("Type a password. This application will calculate it's strength")
weak_password_count = 0
strong_password_count = 0
feedback = []
capital_count = 0
symbol_count = 0
number_count = 0
special_chars = "!@#$%^&*()[];:'?<>.,"

# Check password length
if len(password) < 4:
    weak_password_count += 3
    feedback.append("Your password is too short!")
elif len(password) > 10:
    strong_password_count += 5
else:
    strong_password_count += 2

for p in password:
    if p.istitle():
        capital_count += 1
        strong_password_count += 1

    if p.isdigit():
        number_count += 1
        strong_password_count += 1

    if ord(p) == 32:
        spaces_count += 2
        strong_password_count += 2
    
    # Check if special character is used
    for sc in special_chars:
        if p == sc:
            strong_password_count += 2

if capital_count == 0:
    weak_password_count += 1
    feedback.append("You haven't used capitals in your password!")

if number_count == 0:
    weak_password_count += 1
    feedback.append("You haven't used numbers in your password!")    

if weak_password_count > 0:

    print("Your password is weak!")

    for f in feedback:
        print(f)
        print("\n")

if strong_password_count > 15:
    print("Your password is medium!")

if strong_password_count > 20:
    print("Your password is very strong!")