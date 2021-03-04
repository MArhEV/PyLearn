cities = {
        'kielce': {
            'polska',
            '200 000',
            },
        'berlin': {
            'niemcy',
            '1 000 000',
            },
        'moskwa': {
            'rosja',
            '1 200 000',
            },
        }

for key, values in cities.items():
    print(f'\nMiasto: {key.title()}')
    for value in values:
        new_val = str(value)
        print(f'{value.title()}')

