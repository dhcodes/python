sandwich_orders = ['turkey', 'blt', 'roast beef', 'burger', 'grilled cheese']
finished_sandwiches = []
while sandwich_orders:
    making = sandwich_orders.pop()
    print("I am making your " + making + " sandwich.")
    finished_sandwiches.append(making)
print("\nAll the sandwiches below are now done:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
