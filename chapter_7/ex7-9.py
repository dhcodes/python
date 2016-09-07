sandwich_orders = ['turkey', 'pastrami', 'blt', 'roast beef', 'pastrami', 'burger', 'grilled cheese','pastrami']
print("The deli has run out of pastrami!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for sandwich in sandwich_orders:
    print(sandwich) 
