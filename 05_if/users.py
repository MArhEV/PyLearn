users = ['admin', 'alicja', 'adam', 'szymon', 'jarek']

for user in users:
    if user == 'admin':
        print('Welcome admin! See reports from today.')
    else:
        print("Welcome", user)

print('---------empty list----------')

users = []

if users:
    for user in users:
        if user == 'admin':
            print('Welcome admin! See reports from today.')
        else:
            print("Welcome", user)
else:
    print('List is empty')

print('--------------users-------------')

current_users = ['Alicja', 'Adam', 'Szymon', 'Jarek', 'analdestroyer']
new_users = ['beata', 'asia', 'zjeb', 'analdestroyer']

current_users_lower = [x.lower() for x in current_users]

print(current_users_lower)

if new_users:
    for new_user in new_users:
        if new_user in current_users:
            print('pick another username')
        else:
            print('this username can be used')

print('----------------liczby porzadkowe------------')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print('1st')
    elif number ==2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(number, 'th', sep='')
