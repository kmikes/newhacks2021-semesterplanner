# This is a sample Python script.
#- Main Code Body

user_input = ''
accounts = {
    "Andrew":[10,11],
    "Kaija":[10,14]
}
Username = ""

# Login or add an account
while True:
    print("Hello, hello! Would you like to:\n1. create a new account\n2. login to a previous account\n3. exit")
    user_input = str(input("Your answer:"))
    while user_input != "1" and user_input != "2" and user_input != "3":
        print(user_input)
        user_input = str(input("Invalid"))
    else:
        if user_input == '1':
            Username = input("Create a Username")
            Main_countdowndate = input("Enter the countdown date in the form (month/date/year)")
            numberform= Main_countdowndate.split("/")
            Deadline=input()
            accounts.update({Username : numberform})
            print(accounts)
            #open main screen
        elif user_input == '2':
            Username = input("Input your preciously created account")
            #open the main screen
            Edit_or_look= input("Hello", Username,".\n1.Just look at Countdown\n2. Edit dates")
            if Edit_or_look==1:
                pass
                #Go to countdown
            elif Edit_or_look ==2:
                pass
                #go to edit screen
        elif user_input=="3":
            #close()?
            pass


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
