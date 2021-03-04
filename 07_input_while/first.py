marka = input('Jakiej marki samochód chcesz wypożyczyć? ')
print(f'samochód marki {marka.title()}')

print('\n-----------------------------\n')

prompt = ('Ile osób przy stoliku?')
prompt += ('\nIlość: ')

ilosc = input(prompt)
ilosc = int(ilosc)

if ilosc >= 8:
    print('Trzeba poczewkać na stolik')
else:
    print('jest taki stolik')

print('\n------------------------------\n')

liczba = input('podaj liczbe aby sprawdzic czy jest wielokrotnością 10: ')

liczba = int(liczba)
wynik = liczba % 10

if wynik == 0:
    print(f'Lliczba {liczba} jest wielokrotnością 10')
else:
    print(f'Liczba {liczba} nie jest wielokrotnoscią 10')
