password = input("Type a password. This application will calculate it's strength")
weak_password_count = 0
feedback = []
capital_count = 0
symbol_count = 0
number_count = 0

# Check password length
if len(password) < 4:
    weak_password_count += 1
    feedback.append("Your password is too short!")

for p in password:
    print(p)
    if p.istitle():
        capital_count += 1

    if p.isdigit():
        number_count += 1

if capital_count == 0:
    weak_password_count += 1

if number_count == 0:
    weak_password_count += 1

if weak_password_count > 0:
    for f in feedback:
        print(f)

