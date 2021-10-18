import Account3

def accountCreation():
    creation_email = input("Please enter your new email: ")
    creation_username = input("Please enter your new username: ")
    creation_password = input("Please enter your new password: ")
    Account_file = open("Account3.py", "w")
    Account_file.write('email = "' + creation_email.strip() + '"' + '\n')
    Account_file.write('username = "' + creation_username.strip() + '"' + '\n')
    Account_file.write('password = "' + creation_password.strip() + '"')

def accountVerification():
    asked_email = input('Email: ')
    asked_username = input('Username: ')
    asked_password = input('Password: ')
    verify_password = input('Please verify the password again: ')
    if not verify_password.strip() == asked_password.strip():
        tries = 1
        while verify_password != asked_password and tries != 5:
            verify_password = input("Please verify the password again: ")
            tries += 1
    if asked_email.strip() != Account3.email:
        print("Wrong email!")
    elif asked_username.strip() == Account3.username and asked_password.strip() == Account3.password and asked_email.strip() == Account3.email:
        print("Welcome back " + Account3.username.strip() + "!")
    elif asked_username.strip() == Account3.username and asked_password.strip() != Account3.password:
        print("Wrong username!")
    elif asked_password.strip() == Account3.password and asked_username.strip() != Account3.username:
        print("Wrong password!")
    else:
        print("Wrong username and password")