person = {'first_name': 'marek', 'last_name': 'czekalski', 'age': 23, 'city': 'kielce',}
print(person)

name = person['first_name'].title()
print(name)

possesion = person.get('possesion', 'no possesion declared')
print(possesion.title())

person['possesion'] = 'student'
possesion = person.get('possesion', 'no possesion declared')
print(possesion.title())

print('-------------------FOR-------------------')

for key, value in person.items():
    new_val = str(value)
#    print(new_val)
    print(type(new_val))
#    if type(person[value]) is int:
#        print(f'{key}: {value}')
#    else:
    print(f'{key}: {new_val.title()}')
    print()
