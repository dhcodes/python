sandwiches = ['blt', 'hamburger', 'chicken', 'turkey', 'avocado bacon']
print("Is burrito in sandwiches? Probably not.")
print('burrito' in sandwiches)

print('\nDoes turkey have the same number of letters as chicken? No.')
print(len('turkey') == len('chicken'))

print("\nIs blt a sandwich? I think so!")
print('blt' in sandwiches)

car = 'fast'
print("\nIs the car fast?")
print(car == 'fast')

cars = 2
print("\nDo I own more than 2 cars? Nope, I do not.")
print(cars > 2)

bikes = 3
print("\nDo I own more than 2 bicycles? Yep, yep I do.")
print(bikes > 2 and bikes < 4)

print("\nLet's confirm that a burrito hasn't snuck into sandwiches list.")
print('burrito' not in sandwiches)

print("\nLet's add 'burrito' to sandwiches because a burrito is pretty similar.")
sandwiches.append('burrito')
print('burrito' in sandwiches)

car_wheels = 4
print("\nIf I have 2 cars, I should have 8 wheels.")
print(cars*car_wheels == 8)
