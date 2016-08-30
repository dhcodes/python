#updated from ex6-5.py
rivers = {
'nile': {'country': 'egypt', 'length (mi)':4258, 'discharge':99940, 'wildlife':['crocodiles','birds','hippopotamuses']},
'yellow': {'country': 'china', 'length (mi)':3395, 'discharge':90790, 'wildlife':['geckos','turtles','ostrich']},
'mississippi': {'country': 'US', 'length (mi)':2320, 'discharge':593000, 'wildlife':['snakes','buffalo','molerats']},
}

for key, value in rivers.items():
    print('The ' + key + " river is located in " + value['country']+", has a water discharge rate of " + str(value['discharge']) + " cubic ft/s, and has the following wildlife: ")
    for animal in value['wildlife']:
        print(animal)
