fav_numbers = {'jim':[3, 5], 'ethel': [45, 37], 'tina': [32, 33], 'joey': [20, 1], 'chris': [10, 130]}

for person, nums in fav_numbers.items():
    print("\n" + person.title() + "'s favorite numbers are ")
    for num in nums:
        print("\r"+str(num))
