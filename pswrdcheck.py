file = open("passwords.txt", "r")

for line in file:
    password = line.strip()

    has_upper = False
    has_lower = False
    has_digit = False

    i = 0
    while i < len(password):
        if password[i] >= 'A' and password[i] <= 'Z':
            has_upper = True
        elif password[i] >= 'a' and password[i] <= 'z':
            has_lower = True
        elif password[i] >= '0' and password[i] <= '9':
            has_digit = True
        i = i + 1

    if len(password) < 8:
        print(password, "-> Weak")
    elif has_upper and has_lower and has_digit:
        print(password, "-> Strong")
    else:
        print(password, "-> Medium")

file.close()