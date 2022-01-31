# Authentication Program

# Initialize number of attempts
tries = 0

# Checking credentials
def login(uid, pwd):
    if uid == "ADMIN" and pwd == "St0rE@1" and tries < 3:
        print("Login Successful\n")
        return True
    elif tries < 2:
        print("Try again\n")
        return False
    else:
        print('Account Blocked\n')
        return False

print("Please enter your username and password(You have 3 attempts).\n")
while tries < 3:
    if login(str(input("Username: ")), str(input("Password: "))) is False:
        tries += 1
        continue
    else:
        break