def city_country(city, country):
    return city.title() + ", " + country.title()

nyc = city_country('new york city', 'united states')
paris = city_country('Paris', 'France')
munich = city_country('Munich', 'germany')

print(nyc)
print(paris)
print(munich)
