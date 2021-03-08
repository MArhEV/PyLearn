sandwich_orders = ['salami', 'pastrami', 'szynka', 'ser', 'pastrami', 'panini', 'pastrami']
finished_orders = []

print('skończyło się pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'Przygotowano kanapkę {sandwich.title()}.')

    finished_orders.append(sandwich)

print(finished_orders)

print('\n------ankieta------')
responses = {}

set_active = True
while set_active:
    name = input('podaj swoje imię: ')
    place = input('w jakie miejsce najbardziej chciałbyś sie wybrać? ')

    responses[name] = place
    
    set = input('czy ktos jeszcze chce odpowiedziec? (tak/nie): ')
    if set == 'nie':
        set_active = False

for name, response in responses.items():
    print(f'{name.title()} chciałby odwiedzić {response}.')

