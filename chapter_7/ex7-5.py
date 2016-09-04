age = input("Welcome to the movies. What age are you?")
age = int(age)
if age < 3:
    print("Your ticket is free!")
elif age > 3 and age < 12:
    print("Your ticket is $12.")
else:
    print("Your ticket is $15.")
