magicians = ['jafaar', 'merlin', 'robby']

def show_magicians(list):
    for person in list:
        print(person.title())

def make_great(list):
    for index,person in enumerate(list):
        list[index] = person + " the Great"
    return list



greatMagicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(greatMagicians)
