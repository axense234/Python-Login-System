from Account import saved_username
from Account import saved_password
account_existence = input("Hello,do you have an account? ")
if account_existence.lower() not in "yesno":
    print("Please type Yes if you agree or No if you do not agree next time!")
if account_existence.lower() == "no":
    account_m_process = input("Do you want to make an account? ")
    if account_m_process.lower() in "no":
        print("Got it!")
    elif account_m_process.lower() in "yes":
        print("Please enter your new username and password: ")
        saved_username = input("Username: ")
        saved_password = input("Password: ")
        Account_file = open("Account.py", "w")
        Account_file.write("saved_username = " "\"" + saved_username + "\"" "\n" "saved_password = " "\"" + saved_password + "\"")
        Account_file.close()
        print("Congratulations on the birth of your new account!")
    elif account_m_process.lower() in "no":
        print("Ok!")
    elif account_m_process.lower() not in "yesno":
        print("Please type Yes if you agree or No if you do not agree next time!")
elif account_existence.lower() in "yes" and account_existence.lower() not in "es":
    print("Please enter your username and password: ")
    username = input("Username: ")
    password = input("Password: ")
    if username == saved_username and password == saved_password:
        print("Welcome back " + saved_username + "!")
    elif password == saved_password and not username == saved_username:
        account_username_trying = input("Wrong username,try again? ")
        if account_username_trying.lower() in "yes":
            tries_username = 5
            while tries_username > 0:
                username = input("Username: ")
                tries_username -= 1
                if username == saved_username:
                    print("Welcome back!")
                elif username != saved_username and not tries_username == 1:
                    print("Wrong username!")
                elif tries_username == 1:
                    print("Last chance!")
    elif username == saved_username and not password == saved_password:
        account_password_trying = input("Wrong password,try again? ")
        if account_password_trying.lower() in "yes":
            tries_password = 5
            while tries_password > 0:
                password = input("Password: ")
                tries_password -= 1
                if password == saved_password:
                    print("Welcome back!")
                elif password != saved_password and not tries_password == 1:
                    print("Wrong password!")
                elif tries_password == 1:
                    print("Last chance!")
    else:
        print("No account exists with the info! ")
