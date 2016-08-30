cities = {
'new york city':{'country':'us', 'population':8406000, 'fact':'It can cost over $289k for a 1-year hot dog stand permit in Central Park.'},
'florence':{'country':'italy','population':361579,'fact':'Nearly a third of the world\'s art treasures reside in Florence.'},
'london':{'country':'england', 'population':8674000,'fact':'London is the 6th most expensive city to live in worldwide as of 2016.'}}

for city,info in cities.items():
    print("\nInformation about "+city.title()+":")
    for key,value in info.items():
        print(str(key).title() + ": " + str(value).title())
    print("==========================")
