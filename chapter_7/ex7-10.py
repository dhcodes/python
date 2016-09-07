poll_answers = {}
polling_open = True

while polling_open:
    name = input("What is your name? ")
    response = input("What is your dream vacation? ")

    poll_answers[name] = response

    repeat = input("Does anyone else want to take the poll? ")
    if repeat == 'no':
        polling_open = False

print("----- Dream Vacations -----")
for name, response in poll_answers.items():
    print(name + "'s dream vacation is: " + response + ".")
