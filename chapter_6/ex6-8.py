robby = {'name':'robby', 'owner': 'randy', 'type': 'hippo'}
mercer = {'name':'mercer', 'owner': 'maven', 'type': 'sloth'}
yoko = {'name':'yoko', 'owner': 'yolanda', 'type': 'koala'}

pets = [robby, mercer, yoko]

for pet in pets:
    print("\n"+ pet['name']+"'s owner is " + pet['owner'] + " and it is a " + pet['type']);
