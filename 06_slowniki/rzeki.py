rivers = {'nil': 'egypt', 'vistula': 'poland', 'volga': 'russia'}

for river, country in rivers.items():
    print(f'{river.title()} is located in {country.title()}')

print()

for river in rivers.keys():
    print(f'{river.title()}')
