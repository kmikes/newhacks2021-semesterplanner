# This is a sample Python script.
#- Main Code Body -#

user_input = ''
account = ''

# Login or add an account
while True:
    print("Hello, hello! Would you like to:\n1. create a new account\n2. login to a previous account\n3. exit")
    user_input = input("Your answer:" )

    if user_input == '1':
        print('lol')
    elif user_input == '2':
        print('not yet a feature')
    else:
        break

    # Main screen
    while True:
        print("Hello, hello! Would you like to:\n1. enter the end of semester\n2. enter a new deadline\n3. logout")
        user_input = input("Your answer:")

        if user_input == '1':
            print('END OF SEMESTER')
        elif user_input == '2':
            print('ENTER NEW DEADLINE')
        else:
            print('YOU HAVE LOGGED OUT')
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
