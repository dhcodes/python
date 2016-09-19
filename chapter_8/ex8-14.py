def car_info(make,model,**other_features):
    #make a car dictionary and store car information
    car = {}
    car['manufactured_by'] = make
    car['model'] = model
    for key,value in other_features.items():
        car[key] = value
    return car


first_car = car_info('subaru', 'outback', color='blue', tow_package=True)
second_car = car_info('honda', 'pilot', type='suv', trim="XLE", color="maroon")
cars = []
cars.append(first_car)
cars.append(second_car)

for car in cars:
    print(car)
