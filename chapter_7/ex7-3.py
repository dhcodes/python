userNumber = input("Pick a number, any number:")
userNumber = int(userNumber)
if userNumber % 10 == 0:
    print("That, my friend, is a multiple of ten.")
else:
    print("That is not a multiple of ten.")
