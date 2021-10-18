import Account3

def accountCreation():
    creation_username = input("Please enter your new username: ")
    creation_password = input("Please enter your new password: ")
    Account_file = open("Account3.py", "w")
    Account_file.write('username = "' + creation_username.strip() + '"' + '\n')
    Account_file.write('password = "' + creation_password.strip() + '"')

def accountVerification():
    asked_username = input('Username: ')
    asked_password = input('Password: ')
    verify_password = input('Please verify the password again: ')
    if not verify_password.strip() == asked_password.strip():
        tries = 1
        while verify_password != asked_password and tries != 5:
            verify_password = input("Please verify the password again: ")
            tries += 1
    if asked_username.strip() == Account3.username and asked_password.strip() == Account3.password:
        print("Welcome back " + Account3.username.strip() + "!")
    elif asked_username.strip() == Account3.username and asked_password.strip() != Account3.password:
        print("Wrong username!")
    elif asked_password.strip() == Account3.password and asked_username.strip() != Account3.username:
        print("Wrong password!")
    else:
        print("Wrong username and password")