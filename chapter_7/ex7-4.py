prompt = "What do you want on your pizza? "
prompt += "Enter 'quit' to end the program.  "
topping = ""
while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(topping)
