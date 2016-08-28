pollers = ['paul', 'edward', 'rudolph', 'remi', 'jen']
favorite_languages = {'jen': 'python',    'sarah': 'c',    'edward': 'ruby',    'phil': 'python',    }

for poller in pollers:
    if poller in favorite_languages.keys():
        print("Thanks " + poller + " for taking the poll.")
    else:
        print("Please take our poll, " + poller)
