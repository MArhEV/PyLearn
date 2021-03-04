person1 = {'first': 'marek', 'last': 'czekan', 'city': 'kielce'}
person2 = {'first': 'michał', 'last': 'tyrion', 'city': 'motkowice'}
person3 = {'first': 'bartosz', 'last': 'bogu', 'city': 'wiślica'}

people = [person1, person2, person3]

for person in people:
    print(person)

print('--------------miejsca-------------')

fav_places = {
        'adam': ['rzym', 'wiedeń'],
        'ewa': ['berlin', 'monako'],
        'kain': ['raj', 'nieraj'],
        }

for key, values in fav_places.items():
    print(f'\nUlubione miejsca {key.title()} to:')
    for value in values:
        print(f'{value.title()}')
