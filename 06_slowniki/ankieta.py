fav_lang = {
        'janek': 'python',
        'sara': 'c',
        'edward': 'ruby',
        'paweł': 'python',
        }

people = ['sara', 'paweł', 'bartek', 'kacper']
for name in people:
    if name in fav_lang.keys():
        print(f'{name.title()} thanks for participating')
    else:
        print(f'{name.title()} you should participate in our project')
