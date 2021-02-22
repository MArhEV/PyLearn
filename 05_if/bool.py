car1 = 'subaru'
car2 = 'bmw'
print("czy car1 == 'subaru'?")
print(car1 == 'subaru')

string1 = 'qwerty'
string2 = 'asdfg'
print(f'czy string1 = string2? {string1}, {string2}: ',string1 == string2)

string1 = 'qwerty'
string2 = 'qwertY'
print(f'czy string1 = string2? {string1}, {string2}: ',string1 == string2)
print(f'czy string1 = string2 po funkcji lower? {string1}, {string2.lower()}: ',string1 == string2.lower())

zepsute = ['zawory', 'szyba', 'lusterko']
sprawne = ['lusterko', 'głowica', 'koła']
print('lusterko' in zepsute and 'lusterko' in sprawne)
print('zawory' in zepsute or 'zawory' in sprawne)
