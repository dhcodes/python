person1 = {'first_name':'bob', 'last_name':'barker','city':'los angeles', 'age':92, }
person2 = {'first_name':'randy', 'last_name':'savage','city':'columbus', 'age':58, }
person3 = {'first_name':'joe', 'last_name':'dimaggio','city':'martinez', 'age':84, }
people = [person1, person2, person3]

for person in people:
    print("\nMeet " + person['first_name'] + " " + person['last_name'] + " from " + person['city'] + ", age " + str(person['age']))
