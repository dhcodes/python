pizzas = ["pepperoni", "supreme", "deep-dish", "chicken and bacon"]
friend_pizzas = pizzas[:]
pizzas.append("sausage")
friend_pizzas.append("anchioves")
print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
