favorite_places = {'bobby':['italy', 'canada', 'argentina'], 'laura':['mountains', 'beach','golf course'], 'tony':['home', 'work', 'church']}

for person, places in favorite_places.items():
    print("\n"+person.title()+"'s favorite places are:")
    for place in places:
        print("\t" + place.title())
