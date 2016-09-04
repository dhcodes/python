toppings = "Tell me the toppings for your pizza: "
toppings += "\nType 'all done' when you're finished adding toppings.\n"
active = True
while active:
    onPizza = input(toppings)

    if onPizza == 'all done':
        active = False
    else:
        print("I'll add " + onPizza + "right away.")
