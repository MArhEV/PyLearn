dodatki = []

prompt = 'Napisz jaki chcesz dodatek'
prompt += '\nWpisz koniec aby zakończyć'
print(prompt)

active = True
while active:
    dodatek = input('Wpisz dodatek: ')
    if dodatek == "koniec":
        active = False
    else:
        dodatki.append(dodatek)
print(f'\n{dodatki}')

print('--------------------------\n')

print('podaj ile masz lat\naby zakonczyc wpisz end')

while True:
    wiek = input('wiek: ')
    if wiek == 'end':
        break
    else:
        wiek = int(wiek)

        if wiek < 3:
            print('0zł')
        elif wiek == 3 & wiek < 12:
            print('10zł')
        elif wiek >= 12:
            print('15zł')
        else:
            print('podaj poprawny wiek')




