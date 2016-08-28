rivers = {
'nile': 'egypt',
'yellow': 'china',
'mississippi': 'us'
}

for key, value in rivers.items():
    print("The " + key + " is a large river in " + value)

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)
