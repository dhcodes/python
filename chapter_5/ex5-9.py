usernames = []
if usernames == []:
    print("We need to find some users!")

else:
    for name in usernames:
        if name == 'admin':
            print("Good day, sir. Would you like to see the logs?")
        else:
            print("Greetings, " + name)
