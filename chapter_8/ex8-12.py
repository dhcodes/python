def make_sandwich(*ingredients):
    #print all the ingredients (arguments) on a sandwich
    print('Making a sandwich, topped with: ')
    for i in ingredients:
        print("- " + i)

make_sandwich('bacon', 'lettuce', 'tomato')
