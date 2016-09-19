magicians = ['jafaar', 'merlin', 'robby']

def show_magicians(list):
#print all the magician names
    for person in list:
        print(person.title())

def make_great(list):
#loop through magician list and add 'the Great' to each
    for index,person in enumerate(list):
        list[index] = person + " the Great"
    return list

make_great(magicians)
show_magicians(magicians)
